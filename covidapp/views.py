from django.shortcuts import render
import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "5e7adfacb6msh2471fa1f00a1731p18d733jsnb6c704474107",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()


def index(request):
    totallen = int(response['results'])
    contries = []

    if request.method == 'POST':
        userinput = request.POST['selection']
        for i in range(totallen):
            if userinput == response['response'][i]['country']:
                new = response['response'][i]['cases']['new']
                active = response['response'][i]['cases']['active']
                recovered = int(response['response'][i]['cases']['recovered'])
                critical = response['response'][i]['cases']['critical']
                total = response['response'][i]['cases']['total']
                deaths = int(total) - int(recovered) - int(active)
        for i in range(totallen):
            contries.append(response['response'][i]['country'])
        contries.sort()
        context = {'response': contries, 'new': new, 'active': active, 'recovered': recovered, 'critical': critical,
                   'total': total, 'deaths': deaths, 'userinput': userinput}
        return render(request, 'index.html', context)
    for i in range(totallen):
        contries.append(response['response'][i]['country'])
    contries.sort()
    context = {'response': contries}
    return render(request, 'index.html',context)