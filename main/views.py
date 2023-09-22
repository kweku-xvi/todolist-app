from django.shortcuts import render
from .models import ToDoList
from django.views.generic import CreateView, DeleteView

def home(request):
    return render(request, 'main/home.html')


class CreateToDoListView(CreateView):
    model = ToDoList
    fields = ['name']
    template_name = 'main/create_todo.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def create_items(response, pk):
    todolist = ToDoList.objects.get(id=pk)

    if response.method == 'POST':
        if response.POST.get('save'):
            for item in todolist.item_set.all():
                if response.POST.get('c' + str(item.id)) == 'clicked':
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif response.POST.get('newItem'):
            txt = response.POST.get('new')
            if len(txt) > 2:
                todolist.item_set.create(text=txt, complete=False)
            else:
                print('invalid')
    return render(response, 'main/create_items.html', {'todolist':todolist})


class DeleteToDoListView(DeleteView):
    model = ToDoList
    success_url = '/'
