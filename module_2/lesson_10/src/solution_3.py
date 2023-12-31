workers_list :dict = {"Джон" : 1, "Майк" : 1, "Эмили" : 1}
def workers(workers_list):
    names_worker = list(workers_list.keys())
    values_worker= list(workers_list.values())
    max_kpi = max(values_worker)
    responsible_worker :dict= [name for name, completed in workers_list.items() if completed == max_kpi]

    return responsible_worker

responsible_worker = workers(workers_list)

print(f"Самый отвественный: {responsible_worker}")


""" "Джон" : 1, "Майк" : 1, "Эмили" : 1 """
""" "Анна" : 5, "Боб" : 7, "Сюзан" : 9   """