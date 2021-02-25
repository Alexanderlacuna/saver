

def check_resource_availability(dataset,name=None):
    return True
def create_trait(**kw):
    assert bool(kw.get("dataset")) != bool(
        kw.get('dataset_name')), "Needs dataset ob. or name"

    assert bool(kw.get("name")), "Need trait name"

    if kw.get('dataset_name'):
        if kw.get('dataset_name') != "Temp":
            dataset = create_dataset(kw.get('dataset_name'))

        else:
            dataset = kw.get('dataset')

        if dataset.type == 'Publish':
            permissions = check_resource_availability(
                dataset, kw.get('name'))

        else:
            permissions = check_resource_availability(dataset)
