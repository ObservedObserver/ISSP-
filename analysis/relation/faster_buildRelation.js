const fs = require('fs')
function cosXY (x, y) {
  let xy = 0;
  let x2 = 0;
  let y2 = 0;
  let len = Math.min(x.length, y.length);
  for (let i = 0; i < len; i++) {
    xy += x[i] * y[i]
    x2 += (x[i] * x[i])
    y2 += (y[i] * y[i])
  }
  let ans = xy / (Math.sqrt(x2) * Math.sqrt(y2))
  return ans
}
function getRateList (delta) {
  let rateList = []
  let avgRate = 0
  let num = 0
  for (let company in companyEvent) {
    let yearRange = [
      Math.min(...companyStock[company].map(item => item.time[0])),
      Math.max(...companyStock[company].map(item => item.time[0]))
    ]
    let monthRange = [
      Math.min(...companyStock[company].map(item => item.time[1])),
      Math.max(...companyStock[company].map(item => item.time[1]))
    ]
    let dayRange = [
      Math.min(...companyStock[company].map(item => item.time[2])),
      Math.max(...companyStock[company].map(item => item.time[2]))
    ]
    let vecStock = []
    let vecEvent = []
    for (let y = yearRange[0]; y <= yearRange[1]; y++) {
      for (let m = monthRange[0]; m <= monthRange[1]; m++) {
        for (let d = dayRange[0]; d <= dayRange[1]; d++) {
          let result0 = companyStock[company].find((item) => {
            return item.time[0] === y && item.time[1] === m && item.time[2] === d
          })
          if (typeof result0 !== 'undefined') {
            vecStock.push(Number(result0['升跌$']) || 0)
          } else {
            vecStock.push(0)
          }
          let result1 = companyEvent[company].filter((item) => {
            return item.time[0] === y && item.time[1] === m && item.time[2] === d
          })
          if (result1.length > 0) {
            vecEvent.push(result1.length)
          } else {
            vecEvent.push(0)
          }
        }
      }
    }
    let rate = cosXY(vecEvent, vecStock.slice(delta))
    if (!isNaN(rate)) {
      avgRate += Math.abs(rate)
      num ++
    }
  }
  return avgRate / num
}

let data = JSON.parse(fs.readFileSync('../../dataset/relation/stock&event.json').toString())
let {
  company_event: companyEvent,
  company_stock: companyStock
} = data
let ans = []
for (let i = 0; i <= 100; i++) {
  let val = getRateList(i)
  console.log(i, val)
  ans.push({
    rating: val,
    delta: i
  })
}
fs.writeFileSync('../../dataset/relation/ratings_time_lag_less100.json', JSON.stringify(ans))