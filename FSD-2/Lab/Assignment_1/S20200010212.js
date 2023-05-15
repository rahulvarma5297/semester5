const data_from_csv = `Agartala,Aizawl,342
Aizawl,Imphal,400csv
Amaravathi,Bangalore,663
Amaravathi,Chennai,448
Amaravathi,Bhubaneswar,819
Amaravathi,Raipur,758
Bangalore,Panaji,578
Bangalore,Chennai,333
Bangalore,Thiruvanathapuram,730
Bangalore,Mumbai,980
Bhopal,Gandhinagar,599
Bhubaneswar,Raipur,544
Bhubaneswar,Ranchi,455
Bhubaneswar,Kolkata,441
Chandigarh,Lucknow,742
Chandigarh,Jaipur,528
Chennai,Thiruvanathapuram,771
Dehradun,Lucknow,552
Dispur,Shillong,91
Dispur,Imphal,482
Dispur,Aizawl,462
Dispur,Agartala,536
Dispur,Itanagar,323
Dispur,Kohima,350
Hyderabad,Amaravathi,271
Hyderabad,Bangalore,569
Hyderabad,Raipur,783
Hyderabad,Mumbai,719
Imphal,Kohima,136
Jaipur,Gandhinagar,634
Jaipur,Bhopal,598
Kohima,Itanagar,323
Kolkata,Ranchi,395
Kolkata,Patna,583
Kolkata,Gangtok,675
Kolkata,Dispur,1035
Lucknow,Jaipur,574
Lucknow,Bhopal,615
Lucknow,Ranchi,710
Lucknow,Patna,539
Mumbai,Panaji,542
Mumbai,Gandhinagar,553
Mumbai,Bhopal,776
Patna,Ranchi,327
Raipur,Mumbai,1091
Raipur,Bhopal,614
Raipur,Lucknow,810
Raipur,Ranchi,580
Shimla ,Chandigarh,113
Shimla ,Dehradun,227
Shimla ,Lucknow,841
Srinagar,Shimla,620
Srinagar,Chandigarh,562`

const toks = data_from_csv.split("\n")
let patho

function split_store_in_arr(token){
    let [sour,dest,dis] = token.split(',')
    return {
        source: sour,
        dest: dest,
        dist: dis
    }
}

const final_data = data_from_csv.split("\n").map(split_store_in_arr)

console.log(final_data)

function neighbours_of_city(city){
    const neighbors = final_data.filter(x => x.source == city || x.dest == city)
    return neighbors
}

function short_path(source, dest){
    const temp = [{
        c: source,
        dist: 0
    }]
    const visited_cities = {}
    visited_cities[source] = true
    while(temp.length > 0){
        const {c, dist} = temp.shift()
        if(c == dest){
            for(let r = 0;r < temp.length;r++){
                document.getElementById('r1').innerHTML += ("->" + temp[r].c);
            }
            return dist

            
        }
        const neighbors = neighbours_of_city(c)
        for(let x of neighbors){
            if(!visited_cities[x.dest]){
                visited_cities[x.dest] = true
                temp.push({
                    c: x.dest,
                    dist: dist + parseInt(x.dist)
                })
            }
        }
    }
    return -1
}

function short_path1(source, dest){
    const temp = [{
        c: source,
        dist: 0
    }]
    const visited_cities = {}
    visited_cities[source] = true
    while(temp.length > 0){
        const {c, dist} = temp.shift()
        if(c == dest){
            for(let r = 0;r < temp.length;r++){
                document.getElementById('r2').innerHTML += ("->" + temp[r].c);
            }
            return dist

            
        }
        const neighbors = neighbours_of_city(c)
        for(let x of neighbors){
            if(!visited_cities[x.dest]){
                visited_cities[x.dest] = true
                temp.push({
                    c: x.dest,
                    dist: dist + parseInt(x.dist)
                })
            }
        }
    }
    return -1
}

function any_route(){
    let source_from_dropdown = document.getElementById('source').value;
    let dest_from_dropdown = document.getElementById('destination').value;

    let val1 = short_path(source_from_dropdown, dest_from_dropdown);
    let val2 = short_path(dest_from_dropdown, source_from_dropdown);
    let final_val = Math.max(val1, val2);

    if(final_val == -1){
        alert("Oops!!! No path found, Please try for other cities")
        document.getElementById('route1').innerHTML = "Oops!!!, No path found as per the CSV Data, Please try for other cities";
    }else{
        document.getElementById('route1').innerHTML = final_val;
    }
    
}


function optimal_route(){
    let source_from_dropdown = document.getElementById('source').value;
    let dest_from_dropdown = document.getElementById('destination').value;

    let val1 = short_path1(source_from_dropdown, dest_from_dropdown);
    let val2 = short_path1(dest_from_dropdown, source_from_dropdown);
    let final_val = Math.max(val1, val2);
    
    if(final_val == -1){
        alert("Oops!!! No path found, Please try for other cities")
        document.getElementById('route2').innerHTML = "Oops!!!, No path found as per the CSV Data, Please try for other cities";
    }else{
        document.getElementById('route2').innerHTML = final_val;
    }
}