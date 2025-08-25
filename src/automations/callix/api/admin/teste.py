from src.automations.callix.api.requestions import get_api_callix_data
from src.automations.callix.api.requestions import map_data

data = get_api_callix_data('user_performance_reports', 'rdfcontech', 'c43c806e-9bfc-4a8e-8464-96ee11501cae', '2025-08-01', '2025-08-01')

mapped = map_data(data, 'abstudiocontech')

print(len(mapped))
print(mapped[0:2])
print(mapped)