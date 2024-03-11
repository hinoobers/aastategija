document.querySelector('#button').addEventListener('click', (e) => {
    document.querySelector('.autod').innerHTML = ''
    const mark = document.querySelector('#mark')
    const keretüüp = document.querySelector('#keretüüp')
    const aasta1 = document.querySelector('#aasta1')
    const aasta2 = document.querySelector('#aasta2')
    const läbisõit1 = document.querySelector('#läbisõit1')
    const läbisõit2 = document.querySelector('#läbisõit2')
    const kütus = document.querySelector('#kütus')
    const käigukast = document.querySelector('#käigukast')
    const vedavsild = document.querySelector('#vedavsild')
    e.preventDefault()
    let url = `http://s.hinoob.xyz:7575/search?labisoit1=${läbisõit1.value}&labisoit2=${läbisõit2.value}&kutus=${kütus.value}&aasta1=${aasta1.value}&aasta2=${aasta2.value}&tuup=${vedavsild.value}&kere=${keretüüp.value}%C3%A4ra&kaigukast=${käigukast.value}&mark=${mark.value}&limit=100`
    fetch(url).then(data => {
        return data.json()
    }).then(log => displayData(log))

})


function displayData(info) {
    for (let x in info) {
        let nimi = info[x]['nimi']
        let aasta = info[x]['aasta']
        let labisoit = info[x]['labisoit']
        let kutus = info[x]['kutus']
        let kere = info[x]['kere']
        let kaigukast = info[x]['käigukast']
        let pilt = info[x]['pilt']
        let tyyp = info[x]['tüüp']

        const container = document.createElement('div')
        container.setAttribute('class', 'autoinfo')

        let image = document.createElement('div')
        let imgEl = document.createElement('img')
        imgEl.src = pilt
        imgEl.setAttribute('class', 'thumb')
        image.appendChild(imgEl)

        const year = document.createElement('span')
        year.setAttribute('class', 'year')
        year.innerHTML = aasta
        const mileage = document.createElement('span')
        mileage.setAttribute('class', 'mileage')
        mileage.innerHTML = labisoit
        const fuel = document.createElement('span')
        fuel.setAttribute('class', 'fuel')
        fuel.innerHTML = kutus
        const transmission = document.createElement('span')
        transmission.setAttribute('class', 'transmission')
        transmission.innerHTML = kaigukast
        const bodytype = document.createElement('span')
        bodytype.setAttribute('class', 'bodytype')
        bodytype.innerHTML = kere
        const drive = document.createElement('span')
        drive.setAttribute('class', 'drive')
        drive.innerHTML = tyyp

        let extra = document.createElement('div')
        extra.setAttribute('class', 'extra')

        extra.appendChild(year)
        extra.appendChild(mileage)
        extra.appendChild(transmission)
        extra.appendChild(bodytype)
        extra.appendChild(drive)

        let title = document.createElement('div')
        title.setAttribute('class', 'title')
        let spanTitle = document.createElement('span')
        spanTitle.innerHTML = nimi
        title.appendChild(spanTitle)


        container.append(image)
        container.append(extra)
        container.append(title)

        document.querySelector('.autod').appendChild(container)
        
    }
}
