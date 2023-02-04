func min(vars ...int) int{
    if len(vars) == 0{
        return 0
    }
    min := vars[0] 
    for _, e := range vars{
        if min > e{
            min = e
        }
    }
    return min
}


func minDistance(word1 string, word2 string) int {
    size1 := len(word1)
    size2 := len(word2)
    
    dp := make([][]int, size1+1)
    for i := 0; i < size1+1; i++{
        dp[i] = make([]int, size2+1)
    }
    
    for i := 0; i < size1+1; i++{
        dp[i][0] = i
    }
    
    for j := 0; j < size2+1; j++{
        dp[0][j] = j
    }
    
    for i := 1; i < size1+1; i++{
        for j := 1; j < size2+1; j++{
            if word1[i-1] == word2[j-1]{
                dp[i][j] = dp[i-1][j-1] 
            } else{
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1             
            } 
        }
    }
    
    return dp[size1][size2]
     
}