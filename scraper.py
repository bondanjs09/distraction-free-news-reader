import trafilatura
from trafilatura import metadata


def extract_article(url: str):
    """
    Mengambil judul dan konten utama artikel.
    """

    downloaded = trafilatura.fetch_url(url)

    if downloaded is None:
        raise Exception("Gagal mengambil halaman website.")

    # Extract article metadata
    meta = metadata.extract_metadata(downloaded)

    title = meta.title if meta and meta.title else "Untitled Article"

    # Extract article content
    article = trafilatura.extract(
        downloaded, include_comments=False, include_tables=False, output_format="txt"
    )

    if not article:
        raise Exception("Konten artikel tidak ditemukan.")

    return title, article
