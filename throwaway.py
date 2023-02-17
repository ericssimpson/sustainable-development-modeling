sdg_api = requests.get('https://dashboards.sdgindex.org/static/downloads/SDR2022.json', auth=('sdgindex-guest', 'W4zaVqsGPUrV6KaVDFfY'))
print(sdg_api.status_code)

sdg_data = pd.read_json(json.dumps(sdg_api.json()), dtype=object)
sdg_data.to_csv('out.csv')