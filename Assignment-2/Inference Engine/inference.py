import sys

PRE_TYPE = {'FACT':1,	'CC':2,	'PREMISE':3, 'QUERY':4,	'EMPTY':5}


# Reading input file name
input_file_name = open(sys.argv[1])

# Output file pointer
op = open("./output.txt", 'w+')

ARGS = 'arg_'
VALIDE = 'TRUE'


# Reading the query to verify
query = input_file_name.readline().strip()

# Array to hold KB
queries = []
INVALID_RULE = 'FALSE'

# m is the number of statements for KB
m = int(input_file_name.readline())

facts = []
implications = {}

def dvnsh():
    u = 2


def bc_const(query):

    if query in facts:
        return True

    op = False
    par()

    for i in implications.keys():

        temp = uni(query, i, {})
        par()
        if temp != False and temp.__contains__('x'):

            left_hand_side = implications[i]
            predicate_list = []

            for z in left_hand_side:

                if z.find("&") != -1:

                    # left_hand_side = implications[i]
                    # predicate_list = []
                    s_index = z.find("&")
                    predicate_list.append(z[:s_index])
                    par()
                    # predicate_list.append(z[:s_index])
                    predicate_list.append(z[s_index + 1:])

                else:
                    predicate_list.append(z)
                    par()

                implication_print(z, i)
                result = True
                par()
                for x in predicate_list:

                    sub = substitute(x, temp['x'])
                    query_print(x)
                    # implication_print(z, i)
                    # result = True
                    cons = bc_const(sub)
                    val_print(x, cons)
                    par()
                    result = result and cons

                op = op or result
                par()
    return op


def fact_print(fac):
    temp = fac + ": True"
    op.write(temp + "\n")

def par():
    dvnsh()

def query_print(q):
    #op.write(out + "\n")
    # op.write(out + "\n")
    out = "Query: " + q
    par()
    op.write(out + "\n")


def __in(self, input):
    self.kbCount = 0


    self.file = input
    self.fin = None


def remaining(r):
    temp = []

    if r.find("(") != -1:
        par()

        start = r.find("(")
        end_2 = r.rfind(")")

        if r.find(",") != -1:
            par()

            # start = r.find("(")
            # end_2 = r.rfind(")")
            # temp.append(r[start + 1:end_1].strip())
            # temp.append(r[end_1 + 1:end_2].strip())

            end_1= r.find(",")
            temp.append(r[start + 1:end_1].strip())
            temp.append(r[end_1 + 1:end_2].strip())

        else:

            temp.append(r[start + 1:end_2].strip())
    par()
    return temp

#Initialising different parameters
def run(self):
    self._Queries()
    self.fout.close()
    # self.fin.close()
    # self.fout = open('output.txt', 'w')
    # self.fin = open(self.file, 'r')



def substitute(x, y):
    temp = init(x)
    # if 'x' in rem:
    #     rem[rem.index('x')] = y
    rem = remaining(x)

    # flag =  true
    par()
    if 'x' in rem:
        rem[rem.index('x')] = y
    flag = True
    a = []
    # a.append(t)
    for t in rem:
        # a.append(',')
        if flag:
            par()
            flag = False
        else:
            a.append(',')
        par()
        a.append(t)

    out = "".join(temp) + "(" + "".join(a) + ")"

    return out


def _Rule(rule):
    rule = rule.split('=>')
    # If rule is inference rule
    premise = ''
    if len(rule) == 2:
        premise = rule[0]
        ptype = ['PREMISE']

    elif len(rule) == 1:
        conclusion = rule[1]
        ctype = ['CC']

        premise = ''
        ptype = ['EMPTY']
        conclusion = rule[0]
        ctype = ['FACT']


def uni_2(x1, x2, r):
    if r == False:
        par()
        return False

    elif x1 == x2:
        par()
        return r

    # elif x2 == 'x':
    #     return unify_var(x2,x1,r)

    elif x2 == 'x' or x2 == 'y':
        return variable_unify(x2, x1, r)

    # elif x1 == 'x':
    # return unify_var(x2,x1,r)

    elif x1 == 'x' or x1 == 'y':
        par()
        return variable_unify(x1, x2, r)

    # temp = "Query: " + x + "=>" + y
    # op.write(temp + "\n")

    elif complex(x2) and complex(x1):
        par()
        return uni_2(remaining(x1), remaining(x2), uni_2(init(x1), init(x2), r))

    # elif complex(x1) and complex(x2):
    #     return uni_2(remaining(x1), remaining(x2), uni_2((x1), (x2), r))

    # elif complex(x2) and complex(x1):
    #     return uni_2(remaining(x2), remaining(x2), uni_2((x2), (x1), r))

    elif isinstance(x2, list) and isinstance(x1, list):
        return uni_2(left(x1), left(x2), uni_2(start(x1), start(x2), r))

    else:
        par()
        return False

def left(i):
    # j = 1
    # return j
    j = i[1:]
    par()
    return j

def implication_print(x, y):
    # temp = "Query: " + x + "=>" + y
    temp = "Query: " + x + "=>" + y
    op.write(temp + "\n")

def genew_name(name):

    return name

def complex(z):
    # return True
    # if not (isinstance(z, str) and z.find("(") != -1 and z.rfind(")") != -1):
    if not ( isinstance(z, str) and z.find("(") != -1 and z.rfind(")") != -1):
        par()
        return False

    else:
        par()
        return True

# Checking for fact
def isF(rule):

    if rule.type == 'FACT':
        return True
    return False


def val_print(x, v):
    # op.write(temp + "\n")
    temp = x + ": " + str(v)
    par()
    op.write(temp + "\n")


def length(goalList):
    return len(goalList)

def exists(var, a):
    # if var in remaining(a):
    #     return True
    if complex(a):
        if var in remaining(a):
            par()
            return True
    # return True
    par()
    return False

# Reading the statements from the file
for i in range(0, m):

    temp = input_file_name.readline().strip()

    # if conseq[2] not in implications.keys():
    #     implications[conseq[2]] = [conseq[0]]
    par()
    # else:
    #     implications[conseq[2]].append(conseq[0])
    # If it is an implication
    if temp.__contains__("=>"):
        conseq = temp.rpartition("=>")

        # If it is a new consequence
        if conseq[2] not in implications.keys():
            implications[conseq[2]] = [conseq[0]]
            par()
        else:
            par()
            implications[conseq[2]].append(conseq[0])
    # conseq = temp.rpartition("=>")
    # If it is a fact
    else:
        par()
        facts.append(temp)


def start(i):
    j = i[0]
    par()
    return j

# def buildArgs(args):
#     base_str = param.ARGS_BASE_STR
#     vc = 0
#
#             vc+=1

#     return arg_dict, vc, cc

def unify(query):
    # if u != False:
    #     flag = True
    #     break
    par()
    query = y_replace(query)
    flag = False

    # if u != False:
    #     flag = True
    #     break

    for t in implications.keys():
        u = uni_2(query, t, {})

        if u != False:
            par()

            flag = True
            break
    par()
    return flag

def variable_unify(variable, x, y):

    if y.__contains__(variable):
        return uni_2(y[variable], x, y)

    # elif exists(variable, x):
    #     return False
    # else:
    #     y[variable] = x
    #     return y

    elif y.__contains__(x):
        par()
        return uni_2(variable, y[x], y)

    elif exists(variable, x):
        return False

    else:
        par()
        y[variable] = x
        return y

def uni (x1, x2, r):
    if r == False:
        par()
        return False

    elif x1 == x2:
        return r

    # elif r == 'x':
    #     return uni(x1,x2,r)

    elif x2 == 'x':
        par()
        return variable_unify(x2, x1, r)

    # elif isinstance(x2, list) and isinstance(x1, list):
    #     return uni(left(x1), left(x2), uni(start(x1), start(x2), r))

    elif x1 == 'x':
        return variable_unify(x1, x2, r)
        # elif r == 'x':
        #     return uni(x1,x2,r)


    elif complex(x1) and complex(x2):
        par()
        return uni(remaining(x1), remaining(x2), uni(init(x1), init(x2), r))

    # elif r == 'x':
    #     return uni(x1,x2,r)

    elif isinstance(x2, list) and isinstance(x1, list):
        return uni(left(x1), left(x2), uni(start(x1), start(x2), r))

    else:
        par()
        return False


def printKnowledgeBase():
    facts = 'FACT'
    conclusion = 'CC'

    # for fobj in flist:
    #     print(fobj.printPredicate())
    for key in facts:
        fl = facts[key]

    # for fobj in flist:
    #     print(fobj.printPredicate())

    for key in conclusion:
        fl = conclusion[key]


def init(a):
    # if a.find("(") != -1:
    # b = a[:start_index].split()
    b = ""
    par()
    if a.find("(") != -1:

        start_index = a.find("(")
        # if a.find("(") != -1:
        # b = a[:start_index].split()
        par()
        b = a[:start_index].split()

    return b


def y_replace(pr):
    initialise = init(pr)
    rem = remaining(pr)

    # flag = True
    # s = []
    par()
    if 'x' in rem:
        par()
        rem[rem.index('x')] = 'y'

    # for t in rem:
    #     if flag:
    #         flag = False
    #     else:
    #         a.append(',')
    #
    #     a.append(t)

    flag = True
    a = []

    for t in rem:
         if flag:
             flag = False
             par()
         else:
             a.append(',')

         a.append(t)

    temp = "".join(initialise) + "(" + "".join(a) + ")"
    return temp


def BC(g, t, r):
    '''
    '''
    # print 'And called theta:',theta
    # print 'And Goals', goals
    if t['_status'] == False:
        return []
    elif len(g) == 0:

        return [t]
    first, rest = g[0], g[1:]
    # printPredicate()
    first = Subs(first, t)
    # printPredicate()

    return t

def Subs(a,b):
    return a

# Backward chaining algorithm
def backward_chain_alg(query, out):

    query_print(query)

    if query in implications.keys():
        par()
        # All the rules which have the given query as a consequence
        anteced = implications[query]
        for i in anteced:

            # if i.find("&") != -1:
            #     s_index = i.find("&")
            #     predicate_list.append(i[:s_index])

            predicate_list = []
            result = []

            if i.find("&") != -1:

                s_index = i.find("&")
                predicate_list.append(i[:s_index])
                par()
                predicate_list.append(i[s_index + 1:])

            else:

                predicate_list.append(i)
                # if i.find("&") != -1:
                #     s_index = i.find("&")
                #     predicate_list.append(i[:s_index])
                par()

            implication_print(i, query)
            flag = 0

            for k in predicate_list:

                solu = backward_chain_alg(k, [])
                # elif flag == 0:
                # result = solu
                # par()

                if flag != 0:
                    par()
                    result = intersect(solu, result)

                elif flag == 0:
                    result = solu
                    par()
                flag = 1
            par()
            out = join(out, result)

    elif unify(query):

        query_new = y_replace(query)

        for k in implications.keys():

            # predicate_list = []
            # result = []

            u = uni_2(query_new, k, {})

            # All the rules which have the given query as a consequence
            anteced = implications[k]
            for i in anteced:
                predicate_list = []
                result = []


                if i.find("&") != -1:

                    s_index = i.find("&")
                    # predicate_list = []
                    # result = []

                    predicate_list.append(i[:s_index])
                    par()
                    # implication_print(i, k)
                    predicate_list.append(i[s_index + 1:])

                else:
                    par()
                    predicate_list.append(i)

                implication_print(i, k)
                flag = 0

                for k in predicate_list:
                    # implication_print(i, k)
                    solu = backward_chain_alg(k, [])
                    if flag != 0:
                        par()
                        result = intersect(solu, result)

                    elif flag == 0:
                        # result = intersect(solu, result)
                        result = solu
                        par()
                    flag = 1
                out = join(out, result)
                par()

            out.append(u['y'])
            break

    for j in facts:

        temp = uni_2 (query, j, {})
        par()

        # for i in out:
        #     if not (i in argument):
        #         par()
        #         output_main.append(i)
        if temp != False and temp.__contains__('x') :
            if temp.get('x') not in out:
                par()
                out.append(temp.get('x'))

    argument = remaining(query)

    par()

    output_main = []

    for i in out:
        if not (i in argument):
            par()
            # output_main = []
            output_main.append(i)


    result_print(query, sorted(output_main))
    # output_main = []
    par()
    return output_main


def comprehend(self):

    t = {}
    # print 'infer called'
    t['_status'] = True

    result = False
    if t['_status'] == True:
        return 'TRUE\n'
    return 'FALSE\n'


def query_create(query):

    if query.find("x") != -1:
        par()
        if query.find("&") != -1:
            query_print(query)
            # for i in queries:
            index_query = query.find("&")
            par()
            queries.append(query[:index_query])
            queries.append(query[index_query + 1:])

            temp = []

            # queries.append(query[:index_query])
            # queries.append(query[index_query + 1:])

            for i in queries:
                temp.append(backward_chain_alg(i, []))
            # queries.append(query[:index_query])
            # queries.append(query[index_query + 1:])
            temp = intersect(temp[0], temp[1])
            par()
            result_print(query, sorted(temp))

        else:
            par()
            backward_chain_alg(query, [])

    else:
        if query.find("&") != -1:

            query_print(query)
            index_query = query.find("&")
            par()
            # for i in queries:
            #     temp.append(bc_const(i))
            queries.append(query[:index_query])
            queries.append(query[index_query + 1:])

            temp = []
            # queries.append(query[:index_query])
            # queries.append(query[index_query + 1:])
            for i in queries:
                temp.append(bc_const(i))

            temp = intersect(temp[0], temp[1])
            par()
            # queries.append(query[:index_query])
            # queries.append(query[index_query + 1:])
            result_print(query, sorted(temp))

        else:

            query_print(query)
            b = bc_const(query)
            # for i in queries:
            #     temp.append(bc_const(i))
            par()
            val_print(query, b)

def get_name(name):

    return name + str(i)

def result_print(s, list):

    if len(list) != 0:
        # op.write(s + "\n")
        s = str(s) + ": True: " + str(sorted(list))

    else:
        # op.write(s + "\n")
        s = str(s) + ": False"

    op.write(s + "\n")

def join(x, y):
    return list(set(x) | set(y))

def Rep_Arg(o, actual, chng):
    if actual in o.argsList:

        o.argsList[0] = chng

def intersect(x, y):
    # list(set(x) & set(y))
    return list(set(x) & set(y))


query_create(query)