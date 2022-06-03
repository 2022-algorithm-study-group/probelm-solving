class SnapshotArray {
public:
    int snapId = 0;
    int length;
    unordered_map<int, unordered_map<int, int>> snapshots;
    
    SnapshotArray(int length) {
        
    }
    
    void set(int index, int val) {
        snapshots[this->snapId][index] = val;
    }
    
    int snap() {
        snapshots[this->snapId + 1] = snapshots[this->snapId]; 
        return this->snapId++;
    }
    
    int get(int index, int snapId) {
        return snapshots[snapId][index];
    }
};

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray* obj = new SnapshotArray(length);
 * obj->set(index,val);
 * int param_2 = obj->snap();
 * int param_3 = obj->get(index,snap_id);
 */
