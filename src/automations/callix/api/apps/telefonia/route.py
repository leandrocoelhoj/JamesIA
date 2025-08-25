import requests


def treat_route(route_list):

    data = []
    for route in route_list:
        equipe = route['equipe'].split('-')[1].strip()
        techprefix = route['route'].split('Tech:')[1].split(')')[0].strip()
        nome_rota = route['route'].split('-')[1].split('(')[0].strip()

        data_info = {
            "equipe": equipe,
            "techprefix": techprefix,
            "nome_rota": nome_rota
        }

        data.append(data_info)

    return data

def post_routes(routes):
    r = request.post(url="http://localhost:8000/", json=routes)
    return r.status
