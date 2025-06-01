# django-pra
## アプリケーションの作成方法
1. `python manage.py startapp snippets`のようなコマンドを全体のルートで実行することでadmin.pyやviews.pyが自動的に生成される
2. setttings.pyのINSTALLED_APPに`snippets.apps.SnippetsConfig`よように追加する
