import tkinter as tk
from tkinter import filedialog, messagebox
import os
import datetime

from hash_utils import calculate_hash
from database import save_hash, get_hash


class HashCheckerGUI:

    def __init__(self, root):

        self.root = root
        self.root.title("SecureHashChecker")

        # ウィンドウ設定
        self.root.geometry("600x400")
        self.root.minsize(600, 400)

        self.file_path = None


        # 選択ファイル表示
        self.label = tk.Label(
            root,
            text="ファイルを選択してください",
            wraplength=550
        )

        self.label.pack(pady=10)


        # ファイル選択ボタン
        self.select_btn = tk.Button(
            root,
            text="ファイル選択",
            command=self.select_file
        )

        self.select_btn.pack()


        # ファイル情報
        self.info_label = tk.Label(
            root,
            text="ファイル情報:\n未選択",
            justify="left"
        )

        self.info_label.pack(pady=10)


        # ハッシュ表示
        self.hash_label = tk.Label(
            root,
            text="SHA-256:\n未計算",
            justify="left",
            wraplength=550
        )

        self.hash_label.pack(pady=10)


        # 保存ボタン
        self.save_btn = tk.Button(
            root,
            text="ハッシュ保存",
            command=self.save
        )

        self.save_btn.pack(pady=5)


        # 確認ボタン
        self.check_btn = tk.Button(
            root,
            text="整合性確認",
            command=self.check
        )

        self.check_btn.pack(pady=5)



    def select_file(self):

        path = filedialog.askopenfilename()


        if path:

            self.file_path = path


            self.label.config(
                text=path
            )


            # SHA-256計算
            h = calculate_hash(path)


            self.hash_label.config(
                text=f"SHA-256:\n{h}"
            )


            # ファイル情報取得
            size = os.path.getsize(path)

            modified = os.path.getmtime(path)

            modified_time = datetime.datetime.fromtimestamp(
                modified
            )


            info = (
                f"ファイル名: {os.path.basename(path)}\n"
                f"サイズ: {size:,} bytes\n"
                f"更新日時: {modified_time}"
            )


            self.info_label.config(
                text=info
            )



    def save(self):

        if not self.file_path:
            messagebox.showwarning(
                "警告",
                "ファイルを選択してください"
            )
            return


        h = calculate_hash(
            self.file_path
        )


        save_hash(
            self.file_path,
            h
        )


        messagebox.showinfo(
            "保存",
            "ハッシュを保存しました"
        )



    def check(self):

        if not self.file_path:

            messagebox.showwarning(
                "警告",
                "ファイルを選択してください"
            )

            return


        current = calculate_hash(
            self.file_path
        )


        saved = get_hash(
            self.file_path
        )


        if saved is None:

            messagebox.showwarning(
                "確認",
                "保存済みハッシュがありません"
            )

            return



        if saved == current:

            messagebox.showinfo(
                "結果",
                "Integrity OK\n改ざんなし"
            )

        else:

            messagebox.showwarning(
                "結果",
                "Hash mismatch\n変更されています"
            )