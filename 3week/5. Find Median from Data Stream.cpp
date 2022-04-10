class MedianFinder {
public:
    priority_queue<int> pq1;
    priority_queue<int> pq2;
    
    MedianFinder() {
        
    }
    
    void addNum(int num) {
        if(!pq2.empty() && num > -pq2.top()){
            int v = -pq2.top();
            pq2.pop();
            pq1.push(v);
            pq2.push(-num);
        } else {
            pq1.push(num);
        }
        
        if(pq1.size() > pq2.size() + 1){
            pq2.push(-pq1.top());
            pq1.pop();
        }
    }
    
    double findMedian() {
        if(pq1.size() > pq2.size()){
            return pq1.top();
        }
        int v1 = pq1.top();
        int v2 = -pq2.top();
        return (double)(v1 + v2) / 2;
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */
