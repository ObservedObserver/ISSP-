const fs = require('fs')
let data = JSON.parse(fs.readFileSync('../../dataset/relation/ratings_time_lag_less100_wei_list.json').toString())
let newData = []
data.forEach(arr => {
  newData.push(...arr)
})
fs.writeFileSync('../../dataset/relation/ratings_time_lag_less100_wei_list_fix.json', JSON.stringify(newData))