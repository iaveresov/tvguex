currentI = 0 # Текущий символ выражения для функции разбора (глобальная переменная)
# Класс для состояния НКА
class State:
    currentNumber = 0
    states = [] # глобальный список всех вершин

    def __init__(self):
        self.name = State.currentNumber # в качестве имени присваиваем порядковый номер
        State.states.append(self) # сохраняем новую вершину в глобальном списке вершин (для отладки)
        State.currentNumber += 1
        self.edges = {} # ребра храним в хеш-таблице:
# ключ - символ, значение - список вершин, в которые ведут ребра, помеченные этим символом

    def addEdge(self, symbol, state): # метод добавления ребра с меткой symbol, ведущего в вершину state
        if(not(symbol in self.edges)):
            self.edges[symbol] = []
        self.edges[symbol].append(state)

    def __repr__(self):
        return(str(self.name))

    def __str__(self):
        return(str(self.name))

    def printEdges(self): # печатаем содержимое вершины
        for symbol in self.edges:
            print ("\t'" + symbol + "': " + str(self.edges[symbol]))
# функция печати НКА: выводит все вершины,
# созданные на текущий момент, и их ребра

def printStates():
        for state in State.states:
            print("State " + str(state))
            state.printEdges()
        print()


# мини-класс для хранения НКА - хранит только начальное и конечное состояния НКА
class NSM:
    def __init__(self, start, stop):
        self.startState = start
        self.stopState = stop
    def __repr__(self):
        return("Start state is " + str(self.startState) + ", end state is " + str(self.stopState))

# БАЗИС: создаем НКА для символа
def makeSymbolNSM(symbol):
    start = State()
    stop = State()
    start.addEdge(symbol, stop)
    return NSM(start, stop)

# ИНДУКЦИЯ: создаем автомат для регулярного выражения И
def makeAndNSM(leftNSM, rightNSM):
    for symbol in rightNSM.startState.edges:
        for state in rightNSM.startState.edges[symbol]:
            leftNSM.stopState.addEdge(symbol,state)
    return NSM(leftNSM.startState, rightNSM.stopState)
# ИНДУКЦИЯ: создаем автомат для регулярного выражения ИЛИ

def makeOrNSM(leftNSM, rightNSM):
    start = State()
    stop = State()
    start.addEdge('epsilon',leftNSM.startState)
    start.addEdge('epsilon',rightNSM.startState)
    leftNSM.stopState.addEdge('epsilon', stop)
    rightNSM.stopState.addEdge('epsilon', stop)
    return NSM(start, stop)
# ИНДУКЦИЯ: создаем автомат для регулярного выражения *

def makeClosureNSM(cNSM):
    start = State()
    stop = State()
    cNSM.stopState.addEdge('epsilon', cNSM.startState)
    start.addEdge('epsilon', cNSM.startState)
    start.addEdge('epsilon', stop)
    cNSM.stopState.addEdge('epsilon', stop)
    return NSM(start, stop)

class SAR:
    def __init__(self):
        self.inp = ''
        self.string = ''
        self.i = 0
        self.result = None
        self.in_lang = False
        self.len = 0
        self.tselect = {'1', '0', '('}

    def set_data(self, data):
        self.inp = data

    def set_string(self, string):
        self.string = string

    def Start(self):
        r = self.Term()
        if r:
            s = self.Startix(r)
        else:
            return None
        #if not(self.Term()) : return False
        #if not(self.Startix()) : return False
        return s

    def Startix(self, p):
        if self.i >= self.len: return p
        if self.inp[self.i] == '+':
            self.i += 1
            r = self.Term()
            if r:
                s = makeOrNSM(p,r)
            else: return None
            t = self.Startix(s)
            #if not(self.Term()): return False
            #if not(self.Startix()): return False

            if t : return t
            else : return None
        return p
    def Term(self):
        p = self.Factor()
        if p:
            r = self.Tlist(p)
        else:
            return None
        #if not (self.Factor()): return False
        #if not (self.Tlist()): return False
        return r

    def Factor(self):
        if self.i >= self.len: return None
        if self.inp[self.i] == "(":
            self.i += 1
            p = self.Start()
            #if not(self.Start()): return False
            if p:
                if (self.i < self.len) and self.inp[self.i] == ")":
                    self.i += 1
                else: return None
                q = self.Factorix(p)
                if q:
                    return q
                else:
                    return None
                #if not(self.Factorix()): return False
            else: return None
        else:
            q = self.X()
            if q:
                p = self.Double_Factorix(q)
                return p
    def Double_Factorix(self, cNSM):
        if self.i >= self.len: return cNSM
        if self.inp[self.i] == "*":
            self.i += 1
            if cNSM:
                return makeClosureNSM(cNSM)
            else: return None
        else:
            return cNSM

    def X(self):
        if self.inp[self.i] == '0' or self.inp[self.i] == '1':
            p = makeSymbolNSM(self.inp[self.i])
            self.i += 1
            return p
        else: return None

    def Tlist(self, NSM):
        if self.i >= self.len: return NSM
        if self.inp[self.i] in self.tselect:
            p = self.Factor()
            if p:
                q = self.Tlist(p)
                if q:
                    return makeAndNSM(NSM, q)
            else:
                return None
        return NSM
    def Factorix(self, cNSM):
        if self.i >= self.len: return True
        if self.inp[self.i] == "*":
            self.i += 1
            if cNSM:
                return makeClosureNSM(cNSM)
        return cNSM
    def pars(self, inp):
        self.inp = inp
        self.len = len(inp)
        self.result = self.Start()
        print(bool(self.result))
        if bool(self.result):
            if self.i == self.len:
                return True
            else:
                return False
        else:
            return False

    def emulation_NSM(self):
        is_correct_expr = self.pars(self.inp)
        NSM = self.result
        if is_correct_expr:
            lenght = len(self.string)
            i = 0
            s = self.e_closure({NSM.startState})
            for ch in self.string:
                s = self.e_closure(self.move(s, ch))


            if NSM.stopState in s:
                return True
            else: return False
        else:
            return('Error: uncorrect re')

    def e_closure(self, T):
        stack = list(T)
        e_clous = T
        while stack:
            t = stack.pop()
            if not 'epsilon' in t.edges:
                continue
            for vert in t.edges['epsilon']:
                if vert not in e_clous:
                    e_clous.add(vert)
                    stack.append(vert)
        return e_clous

    def move(self, start_set, ch):
        end  = set({})
        for vert in start_set:
            if ch in vert.edges:
                end = end.union(vert.edges[ch])
        return end


data = "(0+1)*011(0+1)*"# Регулярное выражение задается через глобальную переменную

def main():
    parser = SAR()
    parser.set_data(data)
    parser.set_string('1001')
    print(parser.emulation_NSM())
if __name__ == '__main__':
    main()
