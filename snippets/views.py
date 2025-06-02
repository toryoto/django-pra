from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from snippets.models import Snippet, Comment
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe

from snippets.forms import SnippetForm, CommentForm

@require_safe
def top(request):
    snippets = Snippet.objects.all()
    # テンプレートエンジンに与えるPythonオブジェクト
    # renderの第3引数にMapを渡すと、Templateでオブジェクトにアクセスできるようになる
    context = {"snippets": snippets}
    return render(request, "snippets/top.html", context)

@login_required
def snippet_new(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.created_by = request.user
            snippet.save()
            return redirect(snippet_detail, snippet_id=snippet.pk)
    # postリクエストでない場合はフォームが返される
    else:
        form = SnippetForm()
    return render(request, "snippets/snippet_new.html", {"form": form})
    

@login_required
def snippet_edit(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    if snippet.created_by_id != request.user.id:
        return HttpResponseForbidden("このスニペットの編集は許可されていません。")

    if request.method == "POST":
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return redirect('snippet_detail', snippet_id=snippet_id)
    else:
        form = SnippetForm(instance=snippet)
    return render(request, 'snippets/snippet_edit.html', {'form': form})


def snippet_detail(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    comments = Comment.objects.filter(commented_to=snippet_id).order_by('commented_at')
    comment_form = CommentForm()
    
    print(f"コメント数: {comments.count()}")
    
    return render(request, "snippets/snippet_detail.html", {
        'snippet': snippet,
        'comments': comments,
        'comment_form': comment_form
    })