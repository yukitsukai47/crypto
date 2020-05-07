# crypto.py
crypto.pyはテキストファイル、画像ファイル、動画ファイルなどをパスワードで暗号化・復号を行うことができるアプリケーションです。  
これを使ってパスワードが記述してあるファイルや写真、文書などを暗号化して保存しておくことや、他人に安全に譲渡することが可能です。  

crypto.py is an application that can encrypt and decrypt text files, image files, and video files with passwords.  
You can use this to encrypt and store files, photos, documents, etc. with passwords on them, or transfer them safely to others.

# 動作環境
pycrypto 2.6.1 (検証済み)  
### インストール方法
```
pip install pycrypto
```
or
```
pip3 install pycrypto
```
# 使用方法(How to use)  
```
-暗号化-
cat (暗号化したいファイル) | python3 crypto.py -e > (出力したいファイル名)
```
```
-復号-
cat (復号したいファイル) | python3 crypto.py-d > (出力したいファイル名)
```
<img width="682" alt="screenshot" src="https://user-images.githubusercontent.com/52772923/81274766-b7febb80-908b-11ea-9982-7d558f6d90aa.png">
