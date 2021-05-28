def find_datafields(obj):
    """Return pairs of (`number`, `title`) for all available data fields in
       `obj`.
    """
    token = '/data/title'
    channels = [int(k[1:-len(token)]) for k, _ in obj.items()
                if k.endswith(token)]
    titles = [obj['/{}/data/title'.format(ch)] for ch in channels]
    return zip(channels, titles)


def get_datafields(obj):
    """Return a dictionary of titles and their corresponding data fields.
    """
    return {
        v: obj['/{chnum}/data'.format(chnum=k)]
        for k, v in find_datafields(obj)
    }

def get_datagraphs(obj):
    """ Returns a dictionary containing the graphs. 
    Each graph is built as a list of dictionaries of the curves plot. 
    (only data and description, colors are lost)
    """
    token = '/graph/graph/'
    graphs = [k for k in obj.keys() if k[:-1].endswith(token)]

    ographs = {}
    for g in graphs:
        gname = '_'.join(g.split('/')[-2:])
        curves = []
        for c in obj[g]['curves']:
            curve = {k:c[k] for k in ("description", "xdata", "ydata")}
            curves.append(curve)
        ographs[gname] =  curves
    return ographs
