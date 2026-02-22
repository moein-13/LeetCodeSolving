class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        last_element = -1
        for i in range(len(arr) - 1 , -1 , -1):
            current_element = arr[i]
            arr[i] = last_element
            last_element = max(last_element , current_element)

        return arr