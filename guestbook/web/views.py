from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import Message

# 留言列表
class MessageList(ListView):
    model = Message
    ordering = ['-id']      # 以 id 欄位值由大至小反向排序

# 留言檢視
class MessageDetail(DetailView):
    model = Message

# 新增留言
class MessageCreate(CreateView):
    model = Message
    fields = ['user', 'subject', 'content']     # 僅顯示 user, subject, content 這 3 個欄位
    success_url = '/message/'                   # 新增成功後，導向留言列表
    template_name = 'form.html' 

# 刪除留言
class MessageDelete(DeleteView):
    model = Message
    success_url = '/message/'                # 刪除成功返回留言列表
    template_name = 'confirm_delete.html'