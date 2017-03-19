from django.shortcuts import render
from .models import Users, Nodes, Trajectoryentries
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'paths/index.html')

def getTrajectories(request):

    toNode = Nodes.objects.all()[0]
    fromNode = Nodes.objects.all()[65]

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

        if tocount>0 and fromcount>0 and max(fromdates)>min(todates):
            restraj = list(Trajectoryentries.objects.all().filter(usr_id = usr_id))
            for t in restraj:
                if type(t.end_date_year_month_int) != int:
                    t.end_date_year_month_int = 9999
                    t.save()
                    print(t.end_date_year_month_int)

            restraj.sort(key=lambda x: x.end_date_year_month_int)

            finalrescount = finalrescount+1
            finalres.append(restraj)


    allResults = []
    ri = 0
    for r in finalres:

        ri = ri + 1
        ni = 0
        result = ''
        for u in list(r):

            ni = ni + 1
            node = Nodes.objects.get(node_id = u.node_id).node_title
            if ni == 1:
                result += str(ri) + " (usr#" + str(u.usr_id) + ") : " +  str(node)
            else:
                result += " -> " + str(node)
        allResults += [result]
    print(len(allResults))
    return render(request, 'paths/getTrajectories.html', {'results': allResults})
