class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph={}
        for item in times:
            u,v,w=item[0],item[1],item[2]
            if u not in graph:
                graph[u]=[[v,w]]
            else:
                graph[u]+=[[v,w]]
        current=[K]
        delay={K:0}
        
        while current:
            print(current)
            temp=[]
            for node in current:
                neighbors=[]
                if node in graph:
                    neighbors=graph.get(node)
                for neighbor in neighbors:
                    neighbor_node,latency=neighbor[0],neighbor[1]
                    delay_neighbor=delay[node]+latency
                    if neighbor_node not in delay or delay[neighbor_node]>delay_neighbor:
                        temp.append(neighbor_node)
                        delay[neighbor_node]=delay_neighbor
            current=temp
            
        if len(delay.keys())==N:
            return max(delay.values())
        else:
            return -1
