from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect # type: ignore


# def home(request):
#     return render(request,"tharack/home.html")
# def about(request):
#     return render(request,"tharack/about.html")
# def contact(request):
#     return render(request,"tharack/contact.html")

# def portfolio(request):
#     return render(request,"tharack/portfolio.html")
# def resume(request):

#     return render(request, 'tharack/resume.html')

def collatz(number):
    sequence = [number]

    while number != 1 :
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1
        sequence.append(number)
    return sequence

def graph(request):

    if request.method == "POST":
        try:
            number = request.POST['number']
            print("It is post method")

            sequence_length = []

            x = collatz(int(number))
            y = [y for y in range(len(x))]

            context = {
                "data":x,
                "sequence":y,
                "text":"The visualization of collatz series of  " + str(number),
                'info':"Welcome to collatz App",
                "lists":"",
                "length" : len(x),
                'sequence_length':sequence_length

                }

            context['info'] = f"""
                                For the number {str(x[0])} it has {len(x)} sequences and this is because you take the number and then you
                                devide it by two if it is even or multiply by 3 then plus 1 if it is odd. You continue doing that untill you hit 1.
                                The number must be greater than 1 to allow the series generation
                                .
                            """
            context['lists'] =  f"""Sequence list =  {x}"""
            context['length'] = f""" The number {x[0]} make {len(x)} steps to reach 1."""

            return render(request,"tharack/graph.html",context)
        except:
            return render(request,"tharack/graph.html")

    else:
        # print("it is not recognized as post")
        return render(request,"tharack/graph.html")

