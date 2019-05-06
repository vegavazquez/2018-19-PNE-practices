import http.server
import socketserver
import termcolor
import json
import http.client
from Seq import Seq #we will need it after

PORT = 8000


class TestHandler(http.server.BaseHTTPRequestHandler):

    def tratar_argumentos_peticion(self, path):
        diccionario = dict()
        if "?" in self.path:
            argumentos = self.path.split('?')[1]
            argumentos = argumentos.split(" ")[0]
            trozos = argumentos.split("&")
            for pareja in trozos:
                if '=' in pareja:
                    key = pareja.split("=")[0]
                    value = pareja.split("=")[1]
                    diccionario[key] = value
        return diccionario

    def do_GET(self):
        json_response = False


        termcolor.cprint(self.requestline, 'green')
        codigo_respuesta = 200

        if self.path == "/" or self.path == "/index3.html":
            f = open("index3.html", "r") #opening the options page

            contents = f.read()
            f.close()

        elif "/listSpecies" in self.path: #function that returns the list with or without limit
            try:

                argumentos = self.tratar_argumentos_peticion(self.path)

                if "limit" in argumentos: #if it has limit, take it into account
                    try:
                        limit = int(argumentos['limit'])
                    except: #if it doesnt, return the complete list
                        limit = 0
                else:
                    limit = 0

                print("the limit is", limit)

                conn = http.client.HTTPConnection("rest.ensembl.org") #connecting to the web page
                conn.request("GET", "/info/species?content-type=application/json") #specific ending point

                r1 = conn.getresponse()  # guardar la respuesta

                print()
                print("Response received: ", end='')
                print(r1.status, r1.reason)

                text_json = r1.read().decode("utf-8") #decodifying
                solution = json.loads(text_json)
                list_species = solution['species']

                if (limit == 0):
                    limit = len(list_species) #the whole list
                cont = 0

                if 'json' in argumentos:

                    json_response = True
                    listanueva = list_species[1:limit]

                    contents = json.dumps(listanueva) #changing the whole solution to a json file


                else: #solution in a html file form

                    contents = """
                                            <html>
                                            <bpdy>
                                            <ol>"""
                    for specie in list_species: #iteration
                        contents = contents + "<li>" + specie['display_name'] + "</li>"
                        cont = cont + 1
                        if cont == limit:
                            break

                    contents = contents + """</ol></body></html"""
                conn.close()


            except KeyError:
                codigo_respuesta = 404
                f = open('error.html', 'r')
                contents = f.read()
            except TypeError:
                codigo_respuesta = 404
                f = open('error.html', 'r')
                contents = f.read()




        elif 'karyotype' in self.path:

            try:

                argumentos = self.tratar_argumentos_peticion(self.path)

                specie = argumentos['specie'] #specie in the dict

                conn = http.client.HTTPConnection("rest.ensembl.org") #connecting
                conn.request("GET", "/info/assembly/" + specie + "?content-type=application/json")
                r1 = conn.getresponse()
                text_json = r1.read().decode("utf-8")
                solution = json.loads(text_json)
                list_chromo = solution['karyotype']
                if 'json' in argumentos:
                    json_response = True

                    contents = json.dumps(list_chromo)
                else:

                    contents = """
                                                            <html>
                                                            <bpdy>
                                                            <ol>"""
                    for chromo in list_chromo:
                        contents = contents + "<li>" + chromo + "</li>"

                    contents = contents + """</ol>
                                                         </body>
                                                         </html
                                                         """
                conn.close()
            except KeyError:
                codigo_respuesta = 404
                f = open('error.html', 'r')
                contents = f.read()
            except TypeError:
                codigo_respuesta = 404
                f = open('error.html', 'r')
                contents = f.read()




        elif 'chromosomeLength' in self.path:
            try:
                argumentos = self.tratar_argumentos_peticion(self.path)

                chromo = argumentos['chromo']
                specie = argumentos['specie']

                print("the specie is", specie)
                print("the chromosome is", chromo)

                conn = http.client.HTTPConnection("rest.ensembl.org")
                conn.request("GET", "/info/assembly/" + specie + "?content-type=application/json")
                r1 = conn.getresponse()
                text_json = r1.read().decode("utf-8")
                solution = json.loads(text_json)

                info = solution['top_level_region']

                longitud = 0

                for elemento in info:
                    if elemento['name'] == chromo:
                        longitud = elemento['length']
                    print(longitud)

                if 'json' in argumentos:
                    json_response = True
                    print(info)
                    contents = json.dumps(info)
                else:

                    contents = """
                                                                        <html>
                                                                        <bpdy>
                                                                        <ol>"""

                    contents = contents + "<li>" + str(longitud) + "</li>"

                    contents = contents + """</ol>
                                                                     </body>
                                                                     </html
                                                                     """
                    conn.close()

            except KeyError:
                codigo_respuesta = 404
                f = open('error.html', 'r')
                contents = f.read()
            except TypeError:
                codigo_respuesta = 404
                f = open('error.html', 'r')
                contents = f.read()


        elif '/geneSeq' in self.path:
            try:
                argumentos = self.tratar_argumentos_peticion(self.path)

                gene = argumentos['gene']

                conn = http.client.HTTPConnection("rest.ensembl.org")
                conn.request("GET", "/homology/symbol/human/" + gene + "?content-type=application/json")
                r1 = conn.getresponse()
                text_json = r1.read().decode("utf-8")
                solution = json.loads(text_json)
                identifier = solution['data'][0]['id'] #first you get the identifier

                #then you do a second connection whith the identifier to know the sequence
                conn = http.client.HTTPConnection("rest.ensembl.org")
                conn.request("GET", "/sequence/id/" + identifier + "?content-type=application/json")
                r1 = conn.getresponse()
                text_json = r1.read().decode("utf-8")
                solution = json.loads(text_json)
                list_sequence = solution['seq']

                if 'json' in argumentos:
                    json_response = True

                    contents = json.dumps(list_sequence)
                else:

                    contents = """
                                                    <html>
                                                    <body>
                                <h5>SEQUENCE</h5>
                                """ + list_sequence + """

                                                                    </body>
                                                                     </html
                                                                     """

                    conn.close()



            except KeyError:
                codigo_respuesta = 404
                f = open('error.html', 'r')
                contents = f.read()
            except TypeError:
                codigo_respuesta = 404
                f = open('error.html', 'r')
                contents = f.read()


        elif 'geneInfo' in self.path:
            try:

                argumentos = self.tratar_argumentos_peticion(self.path)

                gene = argumentos['gene']
                conn = http.client.HTTPConnection("rest.ensembl.org")
                conn.request("GET", "/homology/symbol/human/" + gene + "?content-type=application/json")
                r1 = conn.getresponse()
                text_json = r1.read().decode("utf-8")
                solution = json.loads(text_json)
                identifier = solution['data'][0]['id'] #first you get the identifier

                #second connection with the id to know the gene
                conn = http.client.HTTPConnection("rest.ensembl.org")
                print("/overlap/id/" + identifier + "?feature=gene;content-type=application/json")
                conn.request("GET", "/overlap/id/" + identifier + "?feature=gene;content-type=application/json")
                r1 = conn.getresponse()
                text_json = r1.read().decode("utf-8")
                solution = json.loads(text_json)

                start = solution[0]['start']
                end = solution[0]['end']
                length = end - start
                chromo = solution[0]['seq_region_name']

                if 'json' in argumentos:
                    json_response = True

                    #dict to store the multiple information
                    dicinfo = dict()
                    dicinfo['start'] = start
                    dicinfo['end'] = end
                    dicinfo['identifier'] = identifier
                    dicinfo['length'] = length
                    dicinfo['chromo'] = chromo
                    contents = json.dumps(dicinfo)




                else:

                    contents = """
                                                                                        <html>
                                                                                        <bpdy>

                                                                    <h5>
                                                                    start: """ + str(start) + """
                                                                    end:""" + str(end) + """
                                                                    identifier:""" + str(identifier) + """
                                                                    length:""" + str(length) + """
                                                                    chromo:""" + str(chromo) + """</h5>







                                                                                        </body>
                                                                                        </html
                                                                                        """
                conn.close()


            except KeyError:
                codigo_respuesta = 404
                f = open('error.html', 'r')
                contents = f.read()
            except TypeError:
                codigo_respuesta = 404
                f = open('error.html', 'r')
                contents = f.read()







        elif '/geneCal' in self.path:
            try:
                argumentos = self.tratar_argumentos_peticion(self.path)

                gene = argumentos['gene']

                conn = http.client.HTTPConnection("rest.ensembl.org")
                conn.request("GET", "/homology/symbol/human/" + gene + "?content-type=application/json")
                r1 = conn.getresponse()
                text_json = r1.read().decode("utf-8")
                solution = json.loads(text_json)
                identifier = solution['data'][0]['id']


                conn.request("GET", "/sequence/id/" + identifier + "?content-type=application/json")
                r1 = conn.getresponse()
                text_json = r1.read().decode("utf-8")
                solution2 = json.loads(text_json)
                sequence = solution2['seq']

                #calling th object Seq created at the beginning of the course
                s1 = Seq(sequence)
                total = len(sequence)


                #using the function percentage from the object Seq
                percA = s1.perc('A')
                percT = s1.perc('T')
                percG = s1.perc('G')
                percC = s1.perc('C')

                if 'json' in argumentos:
                    json_response = True

                    infor = dict()
                    infor['total'] = total
                    infor['percA'] = percA
                    infor['percT'] = percT
                    infor['percG'] = percG
                    infor['percC'] = percC
                    contents = json.dumps(infor)


                else:

                    contents = """
                                                                                    <html>
                                                                                    <bpdy>

                                                                <h5>
                                                                total: """ + str(total) + """
                                                                percentage A:""" + str(percA) + """
                                                                percentage T:""" + str(percT) + """
                                                                percentage G:""" + str(percG) + """
                                                                percentage C:""" + str(percC) + """</h5>







                                                                                    </body>
                                                                                    </html
                                                                                    """
                conn.close()





            except KeyError:
                codigo_respuesta = 404
                f = open('error.html', 'r')
                contents = f.read()

            except TypeError:
                codigo_respuesta = 404
                f = open('error.html', 'r')
                contents = f.read()


        elif 'geneList' in self.path:
            try:
                argumentos = self.tratar_argumentos_peticion(self.path)

                chromo = argumentos['chromo']

                start = argumentos['start']

                end = argumentos['end']

                print(chromo, start, end)

                conn = http.client.HTTPConnection("rest.ensembl.org")
                conn.request("GET", "/overlap/region/human/" + str(chromo) + ":" + str(start) + "-" + str(
                    end) + "?content-type=application/json;feature=gene;feature=transcript;feature=cds;feature=exon")
                r1 = conn.getresponse()
                text_json = r1.read().decode("utf-8")
                solution = json.loads(text_json)

                if 'json' in argumentos:
                    json_response = True
                    print(solution)
                    contents = json.dumps(solution)

                else:

                    contents = """
                            <html>
                                <head>
                                    <title> PER final </title>
                                    </head>

                                    <body>
                                        <ul>
                            """

                    for item in solution:
                        if (item['feature_type'] == 'gene'):
                            contents = contents + '<li>' + item['external_name'] + str(item['start']) + " " + str(
                                item['end']) + '</li>'

                    contents = contents + """</ul>
                                                                                 </body>
                                                                                 </html>
                                                                                 """
                    conn.close()



            except KeyError:
                codigo_respuesta = 404
                f = open('error.html', 'r')

                contents = f.read()


            except TypeError:
                codigo_respuesta = 404
                f = open('error.html', 'r')

                contents = f.read()

        else:
            codigo_respuesta = 404
            f = open('error.html', 'r')

            contents = f.read()

        self.send_response(codigo_respuesta)

        if json_response:
            self.send_header('content-Type', 'application/json')
        else:
            self.send_header('Content-Type', 'text/html')

        self.send_header('Content-Length', len(str.encode(contents)))

        self.end_headers()

        self.wfile.write(str.encode(contents))

        return

#reuse the PORT

Handler = TestHandler
socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()

print("")
print("Server Stopped")
