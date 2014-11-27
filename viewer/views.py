from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import Http404


pxs = {
   1: {
      'Title': 'Aaron Smith feat. Luvli-Dancin (Krono Extended Remix)',
      'Track': 'http://pixound.ru/audio/3035303871_pYdmnyS1.mp3',
      'Image': 'http://cs1494.vk.me/u18344778/21075740/x_768337e8.jpg'
   },
   2: {
      'Title': 'Линда - Северный ветер',
      'Track': 'http://pixound.ru/audio/1416345005_JDnVow0T.mp3',
      'Image': 'http://cs540103.vk.me/v540103850/2094e/f9aV2AiFGSk.jpg'
   },
   3: {
      'Title': 'Выступление Эдди Мерфи',
      'Track': 'http://pixound.ru/audio/1880461425_VvMHR6Uo.mp3',
      'Image': 'http://planetaua.net/uploads/posts/2011-03/1301170613_3.png'
   }
}


def px(request, id):
	id = int(id)
	
	if id > 3 or id < 1:
		raise Http404

	return render_to_response('main.html', pxs[id])