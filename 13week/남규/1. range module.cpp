class RangeModule {
public:
    map<int, int> intervals;
    
    RangeModule() {
        
    }
    
    void addRange(int left, int right) {
        auto l = intervals.upper_bound(left), r = intervals.upper_bound(right);
        if(l != intervals.begin()){
            l--;
            if(l->second < left){
                l++;
            }
        }
        
        if(l != r){
            left = min(l->first, left);
            right = max((--r)->second, right);
            intervals.erase(l, ++r);
        }
        intervals[left] = right;
    }
    
    bool queryRange(int left, int right) {
        auto it = intervals.upper_bound(left);
        if(it == intervals.begin() || (--it)->second < right){
            return false;
        }
        return true;
    }
    
    void removeRange(int left, int right) {
        auto l = intervals.upper_bound(left), r = intervals.upper_bound(right);
        if(l != intervals.begin()){
            l--;
            if(l->second < left){
                l++;
            }
        }
        
        if(l == r) return;
        
        int l1 = min(left, l->first);
        int r1 = max(right, (--r)->second);
        
        intervals.erase(l, ++r);
        if(l1 < left) intervals[l1] = left;
        if(r1 > right) intervals[right] = r1;
    }
};

/**
 * Your RangeModule object will be instantiated and called as such:
 * RangeModule* obj = new RangeModule();
 * obj->addRange(left,right);
 * bool param_2 = obj->queryRange(left,right);
 * obj->removeRange(left,right);
 */
