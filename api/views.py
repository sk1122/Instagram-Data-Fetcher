from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import JsonResponse
import json

from .getDetails import getData

def filterData(r1, r2):
	data = getData()

	filtered_data = {}

	for key, value in data.items():
		if int(value["followers"]) >= int(r1) and int(value["followers"]) <= int(r2):
			filtered_data[key] = value
	print(filtered_data)
	return filtered_data

def index(request):

	data = getData()
	if request.method == 'POST':
		page = request.GET.get('page')

		data_tuple = tuple(data.items())
		pagination = Paginator(data_tuple, 10)

		try:
			user_data = pagination.page(page)
		except PageNotAnInteger:
			user_data = pagination.page(1)
		except EmptyPage:
			user_data = pagination.page(paginator.num_pages)

		range1 = request.POST.get('range1')
		range2 = request.POST.get('range2')

		user_data = filterData(range1, range2)

		user_data = tuple(user_data.items())

		context = {
			'data': user_data
		}

		return render(request, "insta/index.html", context)
	page = request.GET.get('page')

	data_tuple = tuple(data.items())
	pagination = Paginator(data_tuple, 10)

	try:
		user_data = pagination.page(page)
	except PageNotAnInteger:
		user_data = pagination.page(1)
	except EmptyPage:
		user_data = pagination.page(paginator.num_pages)

	context = {
		'data': user_data
	}


	return render(request, "insta/index.html", context)