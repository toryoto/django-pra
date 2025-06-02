## アプリケーションの作成方法
1. `python manage.py startapp snippets`のようなコマンドを全体のルートで実行することでadmin.pyやviews.pyが自動的に生成される
2. setttings.pyのINSTALLED_APPに`snippets.apps.SnippetsConfig`のように追加する

## 認証機能作成
1. `python manage.py startapp accounts`で認証用アプリケーションセットアップ
2. setttings.pyのINSTALLED_APPに`accounts.apps.AccountConfig`のように追加する
3. 汎用クラスベースビューを使用して、accounts/urls.pyのように、templateで事前定義されたviewを使用できるように設定する

