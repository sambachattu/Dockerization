const express = require('express')

const app = express()
const PORT = 8000

app.get('/',(req,res)=>{
    res.send('Hello from node server')
})

app.listen(PORT,()=>{
    console.log(`App is listening on port ${PORT}`)
})