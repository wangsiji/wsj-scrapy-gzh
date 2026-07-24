#!/usr/bin/env python3
"""
秋秋公众号文章向量索引。
扫描 /home/wangsiji/projects/wsj-scrapy-gzh/ 下 秋秋很开心、秋秋在分享
两个目录的文章，清洗、分块、构建 chroma DB。
被 sync_qiuqiu_articles.py 在新文章下载后自动调用。
"""
import os, re, json, hashlib
import chromadb
from pathlib import Path

SOURCE_DIR = "/home/wangsiji/projects/wsj-scrapy-gzh"
VECTORDB_DIR = os.path.expanduser("~/.hermes/qiuqiu-vectordb")

# 只看秋秋的两个号
TARGET_DIRS = ["《秋秋很开心》", "《秋秋在分享》"]


def clean_text(text):
    """去 CSS、去连续空白、去纯链接行。"""
    # 去第一行的 CSS 块
    text = re.sub(r'^.+?\\\* \{.*?\}|^[^{]*\{.*?\}', '', text, flags=re.DOTALL)
    # 去纯链接行
    text = re.sub(r'https?://\S+', '', text)
    # 压缩空白
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()


def chunk_text(text, max_chars=800):
    """按段落分块，每块不超过 max_chars。"""
    paras = [p.strip() for p in text.split('\n') if p.strip()]
    chunks, buf = [], ""
    for p in paras:
        if len(p) > max_chars:
            # 长段落在句号处分
            for s in re.split(r'(?<=[。！？\n])', p):
                if len(s) < 10:
                    continue
                chunks.append(s.strip()[:max_chars])
            buf = ""
        elif len(buf) + len(p) > max_chars and buf:
            chunks.append(buf.strip())
            buf = p
        else:
            buf = (buf + " " + p).strip()
    if buf:
        chunks.append(buf.strip())
    return chunks


def extract_meta(filepath):
    """从文件提取元数据（标题、日期、作者）。"""
    with open(filepath, encoding='utf-8', errors='replace') as f:
        content = f.read()

    # 标题：第一个分隔线后面的行
    title = ""
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if '===' in line and i > 0 and lines[i - 1].strip():
            title = lines[i - 1].strip()[:80]
            break

    # 日期
    m = re.search(r'原创.*?(\d{4}-\d{2}-\d{2})', content)
    pub_date = m.group(1) if m else ""

    # 原文链接
    url = ""
    m = re.search(r'原文地址.*?(https://mp\.weixin\.qq\.com/[^\s\]\)]+)', content)
    if m:
        url = m.group(1).rstrip('/')

    # 账号名
    account = ""
    m = re.search(r'原创.*?秋秋\s+(开心|在分享)', content)
    if m:
        account = f"秋秋{m.group(1)}"
    else:
        m = re.search(r'原创.*?(秋秋很开心)', content)
        if m:
            account = m.group(1)

    return {
        "title": title,
        "pub_date": pub_date,
        "url": url,
        "account": account or "秋秋",
        "filepath": str(filepath),
    }


def build_index():
    client = chromadb.PersistentClient(path=VECTORDB_DIR)

    # 重建集合
    col_name = "qiuqiu_articles"
    try:
        client.delete_collection(col_name)
    except:
        pass
    collection = client.create_collection(col_name)

    ids, docs, metas = [], [], []
    article_count = 0

    for dir_name in TARGET_DIRS:
        dir_path = os.path.join(SOURCE_DIR, dir_name)
        if not os.path.isdir(dir_path):
            continue

        for fname in sorted(os.listdir(dir_path)):
            if not fname.endswith('.md'):
                continue
            fpath = os.path.join(dir_path, fname)
            meta = extract_meta(fpath)
            if not meta["title"]:
                continue

            with open(fpath, encoding='utf-8', errors='replace') as f:
                raw = f.read()

            clean = clean_text(raw)
            chunks = chunk_text(clean)
            if len(chunks) > 20:
                # 长文章采样，每3段取1段
                chunks = chunks[::3]

            for i, chunk in enumerate(chunks):
                uid = hashlib.md5(f"{fpath}:{i}".encode()).hexdigest()[:32]
                ids.append(uid)
                docs.append(chunk)
                metas.append({**meta, "chunk_index": i})

            article_count += 1

    # 分批写入（chroma 对大批量写入有限制）
    batch_size = 500
    for i in range(0, len(ids), batch_size):
        collection.add(
            ids=ids[i:i + batch_size],
            documents=docs[i:i + batch_size],
            metadatas=metas[i:i + batch_size],
        )

    print(f"✅ 索引构建完成: {len(ids)} 个片段, 来自 {article_count} 篇文章")
    print(f"   存储位置: {VECTORDB_DIR}")


if __name__ == "__main__":
    print("📚 扫描文章...")
    build_index()
