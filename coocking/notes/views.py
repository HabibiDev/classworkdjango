from .models import Note
from .models import NotesItem
from coocking_book.models import Dish
from coocking_book.models import Order
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

# Create your views here.


class AddNoteToDishView(View):
    template_name = 'add_note.html'

    def get(self, request, *args, **kwargs):
        model = Dish.objects.get(id=self.kwargs['dish_id'])
        content_type = ContentType.objects.get_by_natural_key(
            app_label='coocking_book', model='dish')
        notes = Note.objects.filter(
            note_item__content_type=content_type, note_item__object_id=self.kwargs['dish_id'])
        context = {"notes": notes, 'model': model}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        content_type = ContentType.objects.get_by_natural_key(
            app_label='coocking_book', model='dish')
        note_content = request.POST["add_note"]
        note = Note.objects.create(content=note_content)
        NotesItem.objects.create(content_type=content_type, object_id=self.kwargs[
                                 'dish_id'], note=note)
        return redirect(reverse('coocking_book:dish_detail', kwargs={'pk': self.kwargs['dish_id']}))


class AddNoteToOrderView(View):
    template_name = 'add_note.html'

    def get(self, request, *args, **kwargs):
        model = Order.objects.get(id=self.kwargs['order_id'])
        content_type = ContentType.objects.get_by_natural_key(
            app_label='coocking_book', model='order')
        notes = Note.objects.filter(
            note_item__content_type=content_type, note_item__object_id=self.kwargs['order_id'])
        context = {"notes": notes, 'model': model}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        content_type = ContentType.objects.get_by_natural_key(
            app_label='coocking_book', model='order')
        note_content = request.POST["add_note"]
        note = Note.objects.create(content=note_content)
        NotesItem.objects.create(content_type=content_type, object_id=self.kwargs[
                                 'order_id'], note=note)
        return redirect(reverse('coocking_book:order_detail', kwargs={'pk': self.kwargs['order_id']}))


class NoteListView(ListView):

    model = Note
    template_name = 'note_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        content_type = ContentType.objects.get_by_natural_key(
            app_label='coocking_book', model=self.kwargs['model'])
        context['notes'] = Note.objects.filter(
            note_item__content_type=content_type)
        context['model'] = self.kwargs['model'].upper()
        return context
