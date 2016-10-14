import sys
import copy

inputfile = open("sample02.txt", 'r')
outputfile = open("./output.txt", 'w+')


def save_input(inp):
    if inp.__contains__('|'):
        v = inp.split('|')
        var.append(v[0].strip())
        var_parents = v[1].split()
        value_for_bayes_net = []
        value_for_bayes_net.append(var_parents)
        local_cond_probs = {}
        for i in range(0, 2**len(var_parents)):
            key = []
            given_values = inputfile.readline().strip()
            separated_values = given_values.split()
            for j in range(0, len(var_parents)):
                key.append(separated_values[j+1].strip())
            local_cond_probs[tuple(key)] = separated_values[0].strip()
        value_for_bayes_net.append(local_cond_probs)
        bayes_net[v[0].strip()] = value_for_bayes_net
    else:
        var.append(inp)
        given_values_2 = inputfile.readline().strip()
        value_for_bayes_net_2 = []
        value_for_bayes_net_2.append([])
        local_cond_probs_2 = {}
        local_cond_probs_2["nil"] = given_values_2
        value_for_bayes_net_2.append(local_cond_probs_2)
        bayes_net[inp] = value_for_bayes_net_2


def read_inputs(lis):
    if lis.find('*') != -1:
        lis = inputfile.readline().strip()
        read_inputs(lis)
    elif len(lis) != 0:
        save_input(lis)
        lis = inputfile.readline().strip()
        read_inputs(lis)
    else:
        pass


num_of_queries = int(inputfile.readline().strip())
query_list = []
for i in range(0,num_of_queries):
    query_list.append(inputfile.readline().strip())
var = []
input_dict = {}
bayes_net = {}
q_var_dict = {}
inpu = inputfile.readline().strip()
read_inputs(inpu)


def make_query_dict(new_i, new_e, q_num):
    q_dict = {}
    q_var_list = []
    single_input_dict = {}
    evid_dict = {}
    if new_i.__contains__(','):
        newer_i = new_i.split(',')
        for j in newer_i:
            query_var = j.split()
            q_var_list.append(query_var[0])
            q_var_dict[q_num] = q_var_list
            q_dict[query_var[0]] = query_var[2]
    else:
        query_var = new_i.split()
        q_var_dict[q_num] = query_var[0]
        q_dict[query_var[0]] = query_var[2]

    if len(new_e) != 0:
        if new_e.__contains__(','):
            newer_e = new_e.split(',')
            for j in newer_e:
                evid_var = j.split()
                evid_dict[evid_var[0]] = evid_var[2]
        else:
            evid_var = new_e.split()
            evid_dict[evid_var[0]] = evid_var[2]

    single_input_dict['vars'] = q_dict
    single_input_dict['evid'] = evid_dict
    input_dict[q_num] = single_input_dict


def read_queries(q_list):
    for i in q_list:
        k = q_list.index(i)
        i = i[2:len(i)-1]
        if i.__contains__('|'):
            new_i = i.split('|')
            make_query_dict(new_i[0], new_i[1], k)
        else:
            make_query_dict(i, '', k)


read_queries(query_list)
#print("Queries: ", input_dict)
#print("Query variables: ", q_var_dict)
# print("All Variables: ", var)
# print("Bayes Net: ", bayes_net)


def normalize(v):
    summ = 0.0
    for val in v.values():
        summ += val
    for a in v.keys():
        v[a] /= summ
    return v


def prob(variab, value, e_dict, b_net):
    paren = b_net[variab][0]
    if len(paren) == 0:
        pr = b_net[variab][1]['nil']
    else:
        p_vals = [e_dict[p] for p in paren]
        pr = b_net[variab][1][tuple(p_vals)]
    if value == '+':
        return float(pr)
    else:
        return 1.0 - float(pr)


def enum_ask(q_num, query, evidence, net, var_list):
    q = {}
    v_l = copy.deepcopy(var_list)
    v_l.reverse()
    if len(query) > 0:
        for f in ('+', '-'):
            evidence[query] = f
            q[f] = enum_all(v_l, evidence, net)
            del evidence[query]
        return normalize(q)
    else:
        q = enum_all(v_l, evidence, net)
        return q


def enum_all(var_list, evidence, net):
    if len(var_list) == 0:
        return 1.0
    else:
        y = var_list.pop()
        if y in evidence:
            va = prob(y, evidence[y], evidence, net)
            valu = va * enum_all(var_list, evidence, net)
            var_list.append(y)
            return valu
        else:
            summ = 0.0
            evidence[y] = '+'
            vp = prob(y, '+', evidence, net)
            summ += vp * enum_all(var_list, evidence, net)
            del evidence[y]
            evidence[y] = '-'
            vpp = prob(y, '-', evidence, net)
            summ += vpp * enum_all(var_list, evidence, net)
            del evidence[y]
            var_list.append(y)
            return summ


def run_all_queries():
    for m in range(0, len(query_list)):
        if query_list[m].__contains__('|'):
            if isinstance(q_var_dict[m], list):
                new_nomi = input_dict[m]['vars'].copy()
                new_nomi.update(input_dict[m]['evid'])
                #print("new: ", new_nomi)
                outp1 = enum_ask(m, '', new_nomi, bayes_net, var)
                outp2 = enum_ask(m, '', input_dict[m]['evid'], bayes_net, var)
                final_outp = outp1/outp2
                print_output(final_outp)
            else:
                outp = enum_ask(m, q_var_dict[m], input_dict[m]['evid'], bayes_net, var)
                quer_var = q_var_dict[m]
                required_bool = input_dict[m]['vars'][quer_var]
                required_val = outp[required_bool]
                print_output(required_val)
        else:
            outp = enum_ask(m, '', input_dict[m]['vars'], bayes_net, var)
            print_output(outp)


def print_output(p_val):
    outputfile.write(str(format(p_val, '.2f') + '\n'))
run_all_queries()