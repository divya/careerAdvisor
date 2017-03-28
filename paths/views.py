from django.shortcuts import render
from .models import Users, Nodes, Trajectoryentries
from django.http import HttpResponse
from django.utils.encoding import python_2_unicode_compatible

import json


# Create your views here.

def autocomplete_job(request):
    term = request.GET.get('term') #jquery-ui.autocomplete parameter
    jobs = Nodes.objects.filter(node_title__istartswith=term)[:10] #lookup for a city
    res = []
    for j in jobs:
         #make dict with the metadatas that jquery-ui.autocomple needs (the documentation is your friend)
         dict = {'id':j.node_id, 'label':j.__unicode__(), 'value':j.__unicode__()}
         res.append(dict)
    return HttpResponse(json.dumps(res))

def index(request):

    jobs = Nodes.objects.order_by('node_title')
    return render(request, 'paths/index.html', {'jobs': jobs})

def getTrajectories(request):

    fromNode = Nodes.objects.get(node_title=request.POST['fromNode'])
    output = request.POST['output-type']

    if output == "next":
        return nextSteps(request)
        # toNode = Nodes.objects.get(node_title=request.POST['toNode'])
        # resusr = Users.objects.all()
        # finalrescount = 0;
        # finalres = []
        #
        # for ru in resusr:
        #     usr_id = ru.usr_id
        #
        #     cur = Trajectoryentries.objects.all().filter(usr_id = usr_id, node_id = fromNode.node_id)
        #     fromcount = len(cur)
        #     fromdates = [f.end_date_year_month_int for f in cur]
        #
        #     fromdates = [9999 if x == None else x for x in fromdates]
        #
        #     if fromcount>0:
        #         restraj = list(Trajectoryentries.objects.all().filter(usr_id = usr_id))
        #
        #         for t in restraj:
        #             if type(t.end_date_year_month_int) != int:
        #                 t.end_date_year_month_int = 999999
        #                 t.save()
        #
        #         restraj.sort(key=lambda x: x.end_date_year_month_int)
        #
        #         finalrescount = finalrescount+1
        #         finalres.append(restraj)
        #
        # allResults = []
        # decriptions = {}
        # ri = 0
        # for r in finalres:
        #     # r = restraj -> [Trajectoryentry, Trajectoryentry]
        #     ri = ri + 1
        #     ni = 0
        #     result = []
        #     for u in list(r):
        #
        #         ni = ni + 1
        #         node = Nodes.objects.get(node_id = u.node_id)
        #         result += [(u, node)]
        #
        #     allResults += [result]
        #     # [ [(u,node), (u,node), (u,node)], [(u,node), (u,node), (u,node)] ]
        #
        # # if sortType == "similarity":
        # #     allResults = sortBySimilarity(allResults)
        #
        # context = {
        #     'results': allResults,
        #     'fromNode': fromNode
        # }
        # return render(request, 'paths/nextSteps.html', context)

    else:
        toNode = Nodes.objects.get(node_title=request.POST['toNode'])
        resusr = Users.objects.all()
        finalrescount = 0;
        finalres = []

        for ru in resusr:
            usr_id = ru.usr_id

            cur = Trajectoryentries.objects.all().filter(usr_id = usr_id, node_id = toNode.node_id)

            tocount = len(cur)
            todates = [t.end_date_year_month_int for t in cur]

            cur = Trajectoryentries.objects.all().filter(usr_id = usr_id, node_id = fromNode.node_id)
            fromcount = len(cur)
            fromdates = [f.end_date_year_month_int for f in cur]

            fromdates = [9999 if x == None else x for x in fromdates]
            todates = [9999 if x == None else x for x in todates]

            if tocount>0 and fromcount>0 and max(fromdates)<min(todates):
                restraj = list(Trajectoryentries.objects.all().filter(usr_id = usr_id))

                for t in restraj:
                    if type(t.end_date_year_month_int) != int:
                        t.end_date_year_month_int = 999999
                        t.save()

                restraj.sort(key=lambda x: x.end_date_year_month_int)

                finalrescount = finalrescount+1
                finalres.append(restraj)


        allResults = []
        decriptions = {}
        ri = 0
        for r in finalres:
            # r = restraj -> [Trajectoryentry, Trajectoryentry]
            ri = ri + 1
            ni = 0
            result = []
            for u in list(r):

                ni = ni + 1
                node = Nodes.objects.get(node_id = u.node_id)
                result += [(u, node)]

            allResults += [result]
            # [ [(u,node), (u,node), (u,node)], [(u,node), (u,node), (u,node)] ]

        # if sortType == "similarity":
        #     allResults = sortBySimilarity(allResults)

        context = {
            'results': allResults,
            'fromNode': fromNode,
            'toNode': toNode
        }
        return render(request, 'paths/getTrajectories.html', context)

def nextSteps(request):
    fromNode = Nodes.objects.get(node_title=request.POST['fromNode'])
    resusr = Users.objects.all()
    finalrescount = 0;
    finalres = []

    for ru in resusr:
        usr_id = ru.usr_id

        cur = Trajectoryentries.objects.all().filter(usr_id = usr_id, node_id = fromNode.node_id)
        fromcount = len(cur)
        fromdates = [f.end_date_year_month_int for f in cur]

        fromdates = [9999 if x == None else x for x in fromdates]

        if fromcount>0:
            restraj = list(Trajectoryentries.objects.all().filter(usr_id = usr_id))

            for t in restraj:
                if type(t.end_date_year_month_int) != int:
                    t.end_date_year_month_int = 999999
                    t.save()

            restraj.sort(key=lambda x: x.end_date_year_month_int)

            finalrescount = finalrescount+1
            finalres.append(restraj)

    allResults = []
    decriptions = {}
    ri = 0
    for r in finalres:
        # r = restraj -> [Trajectoryentry, Trajectoryentry]
        ri = ri + 1
        ni = 0
        result = []
        for u in list(r):

            ni = ni + 1
            node = Nodes.objects.get(node_id = u.node_id)
            result += [(u, node)]

        allResults += [result]
        # [ [(u,node), (u,node), (u,node)], [(u,node), (u,node), (u,node)] ]

    # if sortType == "similarity":
    #     allResults = sortBySimilarity(allResults)

    context = {
        'results': allResults,
        'fromNode': fromNode
    }
    return render(request, 'paths/nextSteps.html', context)

def sortBySimilarity(request):

    fromNode = Nodes.objects.get(node_title=request.POST['fromNode'])
    toNode = Nodes.objects.get(node_title=request.POST['toNode'])

    resusr = Users.objects.all()
    finalrescount = 0;
    finalres = []

    for ru in resusr:
        usr_id = ru.usr_id

        cur = Trajectoryentries.objects.all().filter(usr_id = usr_id, node_id = toNode.node_id)

        tocount = len(cur)
        todates = [t.end_date_year_month_int for t in cur]

        cur = Trajectoryentries.objects.all().filter(usr_id = usr_id, node_id = fromNode.node_id)
        fromcount = len(cur)
        fromdates = [f.end_date_year_month_int for f in cur]

        fromdates = [9999 if x == None else x for x in fromdates]
        todates = [9999 if x == None else x for x in todates]

        if tocount>0 and fromcount>0 and max(fromdates)<min(todates):
            restraj = list(Trajectoryentries.objects.all().filter(usr_id = usr_id))

            for t in restraj:
                if type(t.end_date_year_month_int) != int:
                    t.end_date_year_month_int = 999999
                    t.save()

            restraj.sort(key=lambda x: x.end_date_year_month_int)

            finalrescount = finalrescount+1
            finalres.append(restraj)


    allResults = []
    decriptions = {}
    ri = 0
    for r in finalres:
        # r = restraj -> [Trajectoryentry, Trajectoryentry]
        ri = ri + 1
        ni = 0
        result = []
        for u in list(r):

            ni = ni + 1
            node = Nodes.objects.get(node_id = u.node_id)
            result += [(u, node)]

        allResults += [result]

    l = []
    for traj in allResults:
        t = ""
        nodes = []
        for n in traj:
            t += n[1].node_title.replace(" ", "")
            nodes += [(n[0], n[1])]
        #    [( "SoftwareEngineerSoft...", [(u,node),(u,node)]  )]
        l += [(t, nodes)]

    l = sorted(l, key=getKey)

    results = []
    for trajectory in l:
        # print(trajectory[1])
        results += [trajectory[1]]

    context = {
        'results': results,
        'fromNode': fromNode,
        'toNode': toNode
    }
    return render(request, 'paths/getTrajectories.html', context)


def getKey(t):
    return t[0]
