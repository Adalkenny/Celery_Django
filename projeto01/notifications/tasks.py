from __future__ import absolute_import

from celery import shared_task

from .models import Livro



@shared_task
def helloWord():
	print('Hello Word!')


@shared_task
def add(x, y):
    return x + y


@shared_task
def cadastrarLivro():

	titulo = 'Atomic Habits'
	subtitulo = 'Atitudes de mudança!'
	autor = 'Dale Carnegie'
	presso = 300.00

	livro = Livro.objects.create(
		titulo=titulo,
		subtitulo=subtitulo,
		autor=autor,
		presso=presso

	)

	print('Acabaste the criar um livro. Awesome Dude!')


@shared_task
def deletarLivro():
	livros = Livro.objects.all()
	livros.delete()
	print('Todos os livros removidos com sucesso!')