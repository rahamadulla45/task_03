from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
       'my_list' : [
       {
         'restaurant_name' : 'Al-makan',
         'food_type' : 'french'
       },
        {
         'restaurant_name' : 'kalicut',
         'food_type' : 'kerala'
       },
        {
         'restaurant_name' : 'kollywood',
         'food_type' : 'tamilnadu'
       }

       ]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    'my_object':{
    
         'restaurant_name' : 'kollywood',
         'food_type' : 'tamilnadu'
       }
    

    }
    return render(request, 'detail.html', context)
