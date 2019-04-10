from __future__ import division
class EstadisticaIII:
    def __init__(self,X,Y=[]):
        self.X = X
        self.Y = Y
        self.n = len(X)
    def Fn(self,y):
        return len([x for x in self.X if x<=y])/self.n
    def KS(self,F):
        Xi = sorted(self.X)
        Dn = []
        for i in range(self.n):
            Dn.append(max((i+1)/self.n-F(Xi[i]),F(Xi[i])-i/self.n))
        D = max(Dn)
        K = np.argmax(Dn)
        Femp = [self.Fn(x) for x in np.arange(min(self.X),max(self.X)+0.02,0.01)]
        F0 = [F(x) for x in np.arange(min(self.X),max(self.X)+0.02,0.01)]
        plt.plot(np.arange(min(self.X),max(self.X)+0.02,0.01),Femp)
        plt.plot(np.arange(min(self.X),max(self.X)+0.02,0.01),F0)
        plt.plot(Xi[K],F(Xi[K]),'g^')
        return D