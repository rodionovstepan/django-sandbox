from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import Http404


images = {
	1: 'http://cs540103.vk.me/v540103850/2094e/f9aV2AiFGSk.jpg',
	2: 'http://cs9705.vk.me/u66748/-7/w_4f49129b.jpg',
	3: 'http://cs1494.vk.me/u18344778/21075740/x_768337e8.jpg'
}


def px(request, id):
	id = int(id)
	
	if id > 3 or id < 1:
		raise Http404

	image = images[id]
	return render_to_response('main.html', {'Title': 'Jamie Woon – Spirits (sy.ic Edit)', 'Image': image})