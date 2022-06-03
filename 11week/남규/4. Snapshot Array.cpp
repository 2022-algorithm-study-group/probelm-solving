// Point: umap을 쓰는 공간이 50000번의 unordered_map 복사가 일어날 수 있는데, call이 50000이 아니라 1억개가 들어온다면 괜찮을까?

class SnapshotArray {
public:
    int snapId = 0;
    int length;
    // Space: 50000
    unordered_map<int, unordered_map<int, int>> snapshots;
    
    SnapshotArray(int length) {
        
    }
    
    // Time Complexity: O(1)
    void set(int index, int val) {
        snapshots[this->snapId][index] = val;
    }
    
    // Copy
    // Time Complexity: O(1)
    int snap() {
        snapshots[this->snapId + 1] = snapshots[this->snapId]; 
        return this->snapId++;
    }
    
    // Time Complexity: O(1)
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
