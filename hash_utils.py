import hashlib


def calculate_hash(file_path, algorithm="sha256"):
    """
    ファイルハッシュ計算
    """

    if algorithm == "sha256":
        hash_func = hashlib.sha256()
    elif algorithm == "sha512":
        hash_func = hashlib.sha512()
    else:
        raise ValueError("Unsupported algorithm")

    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                hash_func.update(chunk)

        return hash_func.hexdigest()

    except FileNotFoundError:
        return None