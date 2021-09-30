# 環境構築

## Dockerの起動
1. VS Codeを起動
2. Remote - Containersをインストール
3. 左下の緑のボタンを押してコンテナを起動

## nvm & yarn インストール

1. 以下のいずれかを実行
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash
```
```
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash
```

2. 以下をprofile file(~/.bash_profile, ~/.zshrc, ~/.profile, ~/.bashrc のいずれか)に記入
```
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
```

3. ファイルを保存（下記のように）
```
source ~/.bash_profile
```

4. yarnをインストール
```
npm install -g yarn
```

5. frontに移動
```
cd front
```

6. package.jsonの内容を読み込む
```
yarn install
```