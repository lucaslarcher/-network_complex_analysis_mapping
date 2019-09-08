import os
import networkx as nx

#sudo apt install python-pip
#sudo pip install networkx
#sudo pip install networkx-neo4j

def remove_characters(text,characters):
    for c in characters:
        text=text.replace(c,'')
    return text

citations_directory = 'citations/citations_of_paper/'
main_papers = 'citations/list.txt'

#create graph
G = nx.Graph()
id_authors = []
id_papers = []

file = open(main_papers, "r")
info = str(file.read())
if(info.find('@')>-1):
    info = info.split("@")
    for data in info:
        if(len(data)>0):
            title = ''
            authors = ''
            year = ''
            journal = ''
            organization = ''
            publisher = ''
            booktitle = ''
            if(data.find('title=')!=-1):
                title = data[data.find("title={")+7:]
                title = title[:title.find("}")]
            else:
                continue
            if(data.find('author=')!=-1):
                authors = data[data.find("author={")+8:]
                authors = authors[:authors.find("}")]
            else:
                continue
            if(data.find('year=')!=-1):
                year = data[data.find("year={")+6:]
                year = year[:year.find("}")]
            else:
                continue
            if(data.find('journal=')!=-1):
                journal = data[data.find("journal={")+9:]
                journal = journal[:journal.find("}")]
            else:
                jornal = ''
            if(data.find('booktitle=')!=-1):
                booktitle = data[data.find("booktitle={")+11:]
                booktitle = booktitle[:booktitle.find("}")]
            else:
                jornal = ''
            if(data.find('publisher=')!=-1):
                publisher = data[data.find("publisher={")+11:]
                publisher = publisher[:publisher.find("}")]
            else:
                publisher = ''
            if(data.find('organization=')!=-1):
                organization = data[data.find("organization={")+14:]
                organization = organization[:organization.find("}")]
            else:
                organization = ''     
            
            #print(title)
            #print(authors)
            #print(year)
            
            #working with authors
            authors = remove_characters(authors,"{}\\'"+'"')
            authors = authors.split(' and ')
            id_authors_of_this_paper = []
            #for eashu author
            for author in authors:
                if(author != 'others'):
                    id_author_bd = -1
                    #looking for author
                    for id_author in id_authors:
                         if(G.nodes[id_author]['name'] == author):
                             id_author_bd = id_author
                             break
                    #if exists, acrescent paper
                    if(id_author_bd != -1):
                        id_authors_of_this_paper.append(id_author_bd)
                    #else create new author
                    else:
                        id_authors_of_this_paper.append(G.number_of_nodes())
                        id_authors.append(G.number_of_nodes())
                        G.add_node(G.number_of_nodes(), node='author',name=author)
            
            #working with paper
            id_paper_bd = -1
            for id_paper in id_papers:
                if(G.nodes[id_paper]['title'] == title):
                    id_paper_bd = id_paper
                    break
   
            if(id_paper_bd == -1):
                id_papers.append(G.number_of_nodes())
                id_paper = G.number_of_nodes()
                G.add_node(G.number_of_nodes(), node='paper',title=title,year=year,booktitle=booktitle, journal=journal,publisher=publisher,organization=organization)
                for id_author in id_authors_of_this_paper:
                    G.add_edge(id_author, id_paper, relation='author_of')
 
file.close()

print(G.number_of_nodes())


if(False):
    for i in id_papers:
        print(G.nodes[i]['title'])
    print(len(id_papers))
    

path = [os.path.join(citations_directory, nome) for nome in os.listdir(citations_directory)]
files = [arq for arq in path if os.path.isfile(arq)]

cont = 0
for f in files:
    file = open(f, "r")
    info = str(file.read())

    cont = cont+1
    if(info.find('@')>-1):
        info = info.split("@")
        for data in info:
            if(len(data)>0):
                title = ''
                authors = ''
                year = ''
                journal = ''
                organization = ''
                publisher = ''
                booktitle = ''
                if(data.find('title=')!=-1):
                    title = data[data.find("title={")+7:]
                    title = title[:title.find("}")]
                else:
                    continue
                if(data.find('author=')!=-1):
                    authors = data[data.find("author={")+8:]
                    authors = authors[:authors.find("}")]
                else:
                    continue
                if(data.find('year=')!=-1):
                    year = data[data.find("year={")+6:]
                    year = year[:year.find("}")]
                else:
                    continue
                if(data.find('journal=')!=-1):
                    journal = data[data.find("journal={")+9:]
                    journal = journal[:journal.find("}")]
                else:
                    jornal = ''
                if(data.find('booktitle=')!=-1):
                    booktitle = data[data.find("booktitle={")+11:]
                    booktitle = booktitle[:booktitle.find("}")]
                else:
                    jornal = ''
                if(data.find('publisher=')!=-1):
                    publisher = data[data.find("publisher={")+11:]
                    publisher = publisher[:publisher.find("}")]
                else:
                    publisher = ''
                if(data.find('organization=')!=-1):
                    organization = data[data.find("organization={")+14:]
                    organization = organization[:organization.find("}")]
                else:
                    publisher = ''     
                
                #print(title)
                #print(authors)
                #print(year)
                
                #working with authors
                authors = remove_characters(authors,"{}\\'"+'"')
                authors = authors.split(' and ')
                id_authors_of_this_paper = []
                #for eashu author
                for author in authors:
                    if(author != 'others'):
                        id_author_bd = -1
                        #looking for author
                        for id_author in id_authors:
                            if(G.nodes[id_author]['name'] == author):
                                id_author_bd = id_author
                                break
                        #if exists, acrescent paper
                        if(id_author_bd != -1):
                            id_authors_of_this_paper.append(id_author_bd)
                        #else create new author
                        else:
                            id_authors_of_this_paper.append(G.number_of_nodes())
                            id_authors.append(G.number_of_nodes())
                            G.add_node(G.number_of_nodes(), node='author',name=author)
                #working with paper
                id_paper_bd = -1
                #looking for papaer im bd
                for id_paper in id_papers:
                    if(G.nodes[id_paper]['title'] == title):
                        id_paper_bd = id_paper
                        break
                #if not find
                if(id_paper_bd == -1):
                    id_papers.append(G.number_of_nodes())
                    id_paper_bd = G.number_of_nodes()
                    G.add_node(id_paper_bd, node='paper',title=title,year=year,booktitle=booktitle, journal=journal,publisher=publisher,organization=organization)
                    for id_author in id_authors_of_this_paper:
                        G.add_edge(id_author, id_paper_bd, relation='author_of')
                
                
                #citation thing
                title_citation = f.split('/')
                title_citation = title_citation[len(title_citation)-1]
                title_citation = title_citation.replace('\\','/')
                
                #find cited paper in bd
                index_paper = -1
                for id_paper in id_papers:
                    if(G.nodes[id_paper]['title'] == title_citation):
                        index_paper = id_paper
                        break
                    
                #not oriented edge
                minor_id_was_the_cited = False 
                if(index_paper < id_paper_bd and index_paper > -1):
                    minor_id_was_the_cited = True
                G.add_edge(index_paper, id_paper_bd, relation='cited_by', cited=index_paper,minor_id_was_the_cited=minor_id_was_the_cited) 
                if(index_paper == -1):
                    print(title_citation)
                    print('erro in citation title')
                        
    file.close()
            
    
#create authors graph------------------------------------------------
def get_authors_of(title):
    id_authors_of_this_paper = []
    for id_paper in id_papers:
        if(G.nodes[id_paper]['title'] == title):
            relations_with = G.edges(id_paper)
            for relation in relations_with:
                relation = remove_characters(str(relation),'() ')
                relation = int(relation.split(',')[1])
                if(G.get_edge_data(id_paper,relation)['relation'] == 'author_of'):
                    id_authors_of_this_paper.append(relation)
    return id_authors_of_this_paper

def get_id_author(name):
    for id_author in range(A.number_of_nodes()):
        if(A.nodes[id_author]['name'] == name):
            return id_author
    return -1

def get_id_author_Base(name,B):
    for id_author in range(B.number_of_nodes()):
        if(B.nodes[id_author]['name'] == name):
            return id_author
    return -1

def get_papers_of_author(author):
    papers = []
    for p in id_papers:
        authors = get_authors_of(G.nodes[p]['title'])
        for a in authors:
            if(G.nodes[a]['name'] == author):
                papers.append(p)
    return papers

A = nx.Graph()

#copy id of papers
aux_id_papers = []
for id_paper in id_papers:
    aux_id_papers.append(id_paper)
    
#for each paper
for id_paper in aux_id_papers:
    #get authors of paper
    ids = get_authors_of(G.nodes[id_paper]['title'])
    ids_in_this_paper = []
    #for each author in G, get id in A
    for id_authorG in ids:
        name = G.nodes[id_authorG]['name']
        id_authorA = get_id_author(name)
        #if needs, create a new author
        if(id_authorA == -1):
            id_authorA = A.number_of_nodes()
            A.add_node(id_authorA,name=name,year=G.nodes[id_paper]['year'])    
        ids_in_this_paper.append(id_authorA)
    #do all work together
    for i in range(len(ids_in_this_paper)):
        for a in range(len(ids_in_this_paper)):
            if(i!=a):
                edge = A.get_edge_data(ids_in_this_paper[a],ids_in_this_paper[i])
                weight = 1
                if(edge != None):
                    papers = edge['papers']
                    anotate = False
                    for p in papers:
                        if(p == G.nodes[id_paper]['title']):
                            anotate = True
                            break
                    if(not anotate):
                        weight = weight + int(edge['weight'])
                        papers.append(G.nodes[id_paper]['title'])
                        A.add_edge(ids_in_this_paper[a],ids_in_this_paper[i],relation='work_with', weight=weight, papers=papers)
                else:
                    papers = []
                    papers.append(G.nodes[id_paper]['title'])
                    A.add_edge(ids_in_this_paper[a],ids_in_this_paper[i],relation='work_with', weight=weight, papers=papers)



def get_coautory_newtwork_in_time(begin,end):
    C = nx.Graph()
    
    #copy id of papers
    aux_id_papers = []
    for id_paper in id_papers:
        if(int(G.nodes[id_paper]['year']) >= begin and int(G.nodes[id_paper]['year']) <= end):
            aux_id_papers.append(id_paper)
    
    #for each paper
    for id_paper in aux_id_papers:
        #get authors of paper
        ids = get_authors_of(G.nodes[id_paper]['title'])
        ids_in_this_paper = []
        #for each author in G, get id in A
        for id_authorG in ids:
            name = G.nodes[id_authorG]['name']
            id_authorA = get_id_author_Base(name,C)
            #if needs, create a new author
            if(id_authorA == -1):
                id_authorA = C.number_of_nodes()
                C.add_node(id_authorA,name=name,year=G.nodes[id_paper]['year'])    
            ids_in_this_paper.append(id_authorA)
        #do all work together
        for i in range(len(ids_in_this_paper)):
            for a in range(len(ids_in_this_paper)):
                if(i!=a):
                    edge = C.get_edge_data(ids_in_this_paper[a],ids_in_this_paper[i])
                    weight = 1
                    if(edge != None):
                        papers = edge['papers']
                        anotate = False
                        for p in papers:
                            if(p == G.nodes[id_paper]['title']):
                                anotate = True
                                break
                        if(not anotate):
                            weight = weight + int(edge['weight'])
                            papers.append(G.nodes[id_paper]['title'])
                            C.add_edge(ids_in_this_paper[a],ids_in_this_paper[i],relation='work_with', weight=weight, papers=papers)
                    else:
                        papers = []
                        papers.append(G.nodes[id_paper]['title'])
                        C.add_edge(ids_in_this_paper[a],ids_in_this_paper[i],relation='work_with', weight=weight, papers=papers)
    
    return C


# rede de coautoria e colo ela foi desenvolvida no tempo

#a toutra deve ser uma rede de citações, verificando como as pessoas se citam, 
#quem cita o que, se há muitas autocitações e como é a evolução disso no tempo
               

                
#return ids to citantion od selected paper
def get_citations_of_paper(title):
    index_paper = -1
    for id_paper in id_papers:
        if(G.nodes[id_paper]['title'] == title):
            index_paper = id_paper
            break
    edges = G.edges(index_paper)
    edges = str(edges)
    edges = remove_characters(edges,'[]() ')
    edges = edges.split(',')
    aux_ids = []
    for edge in edges:
        if(int(edge) != id_paper):
            if(G.get_edge_data(id_paper,int(edge))['relation'] == 'cited_by'):
                if(int(edge) > id_paper):
                    if(G.get_edge_data(id_paper,int(edge))['minor_id_was_the_cited']):
                        aux_ids.append(int(edge))
                else:
                    if(not G.get_edge_data(id_paper,int(edge))['minor_id_was_the_cited']):
                        aux_ids.append(int(edge))
    return aux_ids
    
    
get_citations_of_paper('Analysis and optimization of big-data stream processing')


def get_coauthoring_groups():
    groups = []
    boolean_authors = []
    #populating assertion array(True or False)
    for a in range(A.number_of_nodes()):
        boolean_authors.append(True)
    
    #initial author
    id_authorA = 0
    
    while(id_authorA != -1):
        #if exists author, looking for his coautory
        coautory = []
        coautory.append(id_authorA)
        change = True
        while(change):
            change = False
            for c in coautory:
                #get relationships
                edges = A.edges(c)
                edges = remove_characters(str(edges),'[]() ')
                edges = edges.split(',')
                info = []
                for e in edges:
                    if(e != ''):
                        if(e != str(c)):
                            info.append(int(e))
                #looking inf new authores are add in coautory
                for i in info:
                    for j in coautory:
                        exist = False
                        if(i == j):
                            exist = True
                            break
                    if(not exist):
                        coautory.append(i)
                        change = True
        #print(coautory)
        
        if(coautory[0] != -1):
            for k in coautory:
                boolean_authors[k] = False
            groups.append(coautory)
        
        #selection not inserted author
        id_authorA = -1
        for a in range(A.number_of_nodes()):
            if(boolean_authors[a]):
                boolean_authors[a] = False
                id_authorA = a
                break
            
    return groups

def get_coauthoring_groups_in_time(begin,end):
    groups = get_coauthoring_groups()
    year_groups = []
    for i in groups:
        new_group = []
        for j in i: 
            if(int(A.nodes[j]['year']) >= begin and int(A.nodes[j]['year']) <= end):
                new_group.append(j)
        if(len(new_group) > 0):
            year_groups.append(new_group)
    return year_groups

#author works citations
def get_citation_of_author_works(author):
    index_author = -1
    #find author
    for a in id_authors:
        if(G.nodes[a]['name'] == author):
            index_author = a
            break
    #if exists
    if(index_author != -1):
        #get relatioships
        edges = G.edges(index_author)
        edges = remove_characters(str(edges),'[]() ')
        edges = edges.split(',')
        works_of_author = []
        for e in edges:
            if(e != str(index_author)):
                if(G.nodes[int(e)]['node'] == 'paper'):
                    works_of_author.append(int(e))
        citations = []
        for w in works_of_author:
            cs = get_citations_of_paper(G.nodes[w]['title'])
            for c in cs:
                exists = False
                for b in citations:
                    if(c == b):
                        exists = True
                        break
                if(not exists):
                    citations.append(c)
    return citations
    
#authors of author works citations
def get_autors_citatition_of_author(author):
    citations_papers = get_citation_of_author_works(author)
    citation_authors = []
    for cp in citations_papers:
        authors = get_authors_of(G.nodes[cp]['title'])
        for a in authors:
            exists = False
            for ca in range(len(citation_authors)):
                if(citation_authors[ca][0] == a):
                    citation_authors[ca][1] = citation_authors[ca][1] + 1
                    exists = True
                    break
            if(not exists):
                info = []
                info.append(a)
                info.append(1)
                citation_authors.append(info)
    return citation_authors

#authors of author works citations
def get_autors_citatition_of_author_in_time(author,begin,end):
    citations_papers = get_citation_of_author_works(author)
    citation_authors = []
    for cp in citations_papers:
        if(int(G.nodes[cp]['year']) >= begin and int(G.nodes[cp]['year']) <= end):
            authors = get_authors_of(G.nodes[cp]['title'])
            for a in authors:
                exists = False
                for ca in range(len(citation_authors)):
                    if(citation_authors[ca][0] == a):
                        citation_authors[ca][1] = citation_authors[ca][1] + 1
                        exists = True
                        break
                if(not exists):
                    info = []
                    info.append(a)
                    info.append(1)
                    citation_authors.append(info)
    return citation_authors

def check_autocitation(author):
    index_author = -1
    for a in id_authors:
        if(G.nodes[a]['name'] == author):
            index_author = a
            break
    if(index_author != -1):
        authors = get_autors_citatition_of_author(author)
        for i in authors:
            if(i[0] == index_author):
                return i[1]
    return 0


def check_autocitation_in_time(author,begin,end):
    index_author = -1
    for a in id_authors:
        if(G.nodes[a]['name'] == author):
            index_author = a
            break
    if(index_author != -1):
        authors = get_autors_citatition_of_author_in_time(author,begin,end)
        for i in authors:
            if(i[0] == index_author):
                return i[1]
    return 0
            

def get_citation_network_in_time(begin,end):
    C = get_coautory_newtwork_in_time(begin,end)
    D = nx.Graph()
    for a in range(C.number_of_nodes()):
        authors_citation = get_autors_citatition_of_author_in_time(C.nodes[a]['name'],begin,end)
        id_author = D.number_of_nodes()
        D.add_node(id_author,name = C.nodes[a]['name'])
        for i in authors_citation:
            index = get_id_author_Base(G.nodes[i[0]]['name'],D)
            if(index == -1):
                index = D.number_of_nodes()
                D.add_node(index,name=G.nodes[i[0]]['name'])
            cited_id_lesser_then_citator = False
            if(id_author < index):
                cited_id_lesser_then_citator = True
            D.add_edge(id_author,index,weight=i[1],cited_id_lesser_then_citator=cited_id_lesser_then_citator)
    return D

def get_publications_per_year():
    years = []
    for id_paper in id_papers:
        year = int(G.nodes[id_paper]['year'])
        exists = False
        for y in range(len(years)):
            if(years[y][0] == year):
                exists = True
                years[y][1] = years[y][1] + 1
                break
        if(not exists):
            info = []
            info.append(year)
            info.append(1)
            years.append(info)
    year_min = 9999
    year_max = 0
    for y in years:
        if(year_min > y[0]):
            year_min = y[0]
        if(year_max < y[0]):
            year_max = y[0]
    aux = []
    for y in range(year_min,year_max+1):
        info = []
        info.append(y)
        weight = 0
        for i in years:
            if(i[0]==y):
                weight = i[1]
                break
        info.append(weight)
        aux.append(info)
    return aux
        
                
#print distribuition papers in time
if(False):
    import matplotlib as plt

    distribuition_by_year = get_publications_per_year()
    x = []
    y = []
    for a in distribuition_by_year:
        x.append(str(a[0]))
        y.append(a[1])
    plt.rcParams['xtick.labelsize'] = 7
    plt.pyplot.grid()
    plt.pyplot.bar(x, y, color='green')
    plt.pyplot.plot(x, y, '--',color='black')
    plt.pyplot.show()
    


if(False):
    list_tests = [2014,2015,2016,2017,2018,2019]
    for l in list_tests:
        print(str(l)+'++++++++++++++++++++++++++++++++++++++++++++++++')
        print('GRAFO DE CITAÇÕES')
        C = get_citation_network_in_time(0,l)
        cc = list(nx.connected_components(C))
        print('componets conexas: '+str(len(cc)))
        single_componets = 0
        print('tamanho das componentes conexas com mais de um elemento:')
        for i in cc:
            if(len(i) == 1):
                single_componets = single_componets + 1
            else:
                print(len(i))
        print('quantidade de components conexas com 1 item: '+str(single_componets))
        nx.pagerank(C,weight='weight')
        pagerank = nx.pagerank(C,weight='weight')
        pagerank = str(pagerank)
        pagerank = remove_characters(pagerank,'{} ')
        pagerank = pagerank.split(',')
        aux = []
        for pg in pagerank:
            pg = pg.split(':')
            info = []
            info.append(int(pg[0]))
            info.append(float(pg[1]))
            aux.append(info)
        pagerank.clear()
        for pg in aux:
            if(pg[1] > 0.01):
                pagerank.append(pg)
        print('------------------------------------\ntop pagerank')
        
        for pg in pagerank:
            print(C.nodes[pg[0]]['name']+' '+str(pg[0]))
            print(pg[1])
            authors = get_autors_citatition_of_author_in_time(C.nodes[pg[0]]['name'],0,l)
            papers = get_papers_of_author(C.nodes[pg[0]]['name'])
            print('autocitação: '+str(check_autocitation_in_time(pg[0],0,l)))
            print('PAPERS=:')
            for p in papers:
                print('\t'+'> '+G.nodes[p]['title'])
                print('\t'+'+ numero de citações: '+str(len(get_citations_of_paper(G.nodes[p]['title']))))
        
        #betweennes = nx.betweenness_centrality(C,weight='weight')
        #print(betweennes)
    #publications start to grow from 2014

if(True):
    list_tests = [2014,2015,2016,2017,2018,2019]
    coatoring = []
    id_base_authors = []
    for l in list_tests:
        info = []
        c = get_coauthoring_groups_in_time(0,l)
        coatoring.append(c)
        for i in c:
            info.append(i[0])
        id_base_authors.append(info)
        
    print("quantidade de grupos por ano: ")
    for c in range(len(id_base_authors)):
        print(len(id_base_authors[c]))
    
    print('CRESCIMENTO')
    for m in range(len(list_tests)-1):
        print('Crescimento no período '+str(list_tests[m])+' a '+str(list_tests[m+1]))
        for i in id_base_authors[m]:
            #find group in 2014 and before
            for j in coatoring[m]:
                for k in j:
                    if(i == k):
                        begin = len(j)
                        c = c+1
            for j in coatoring[m+1]:
                for k in j:
                    if(i == k):
                        end = len(j)
                        b = b+1
            if(begin < end):
                print(str(begin)+' ->  '+str(end))


        #find group in 2015 and before

            
#fazer a análise do crescimento da rede de coautoria durante o tempo
#quantoficação dos grupos, 
#authors = get_autors_citatition_of_author_in_time('Hesse, Guenter',0,2009)

#print (nx.pagerank(C,weight='weight'))  

