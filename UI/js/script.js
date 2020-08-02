Plotly.d3.csv('../new3d.csv', function(err, rows){
    function unpack(rows, key) {
        return rows.map(function(row)
        { return row[key]; });}
    
    var obj1 = {
        x:unpack(rows, 'x1'), y: unpack(rows, 'y1'), z: unpack(rows, 'z1'), file: unpack(rows,'f1'),
        mode: 'markers',
        marker: {
            color: 'rgb(255, 0, 0)',
            size: 1,
            line: {
                color: 'rgb(255, 0, 0)',
            width: 0.5},
            opacity: 0.8},
        name: 'C_id_0',
        type: 'scatter3d',
    };
    
    var obj2 = {
        x:unpack(rows, 'x2'), y: unpack(rows, 'y2'), z: unpack(rows, 'z2'), file: unpack(rows,'f2'),
        mode: 'markers',
        marker: {
            color: 'rgb(0, 255, 0)',
            size: 1,
            line: {
                color: 'rgb(0, 255, 0)',
            width: 0.5},
            opacity: 0.8},
        name: 'C_id_1',
        type: 'scatter3d'
    };
    
    var obj3 = {
        x:unpack(rows, 'x3'), y: unpack(rows, 'y3'), z: unpack(rows, 'z3'), file: unpack(rows,'f3'),
        mode: 'markers',
        marker: {
            color: 'rgb(0, 0, 255)',
            size: 1,
            line: {
                color: 'rgb(0, 0, 255)',
            width: 0.5},
            opacity: 0.8},
        name: 'C_id_2',
        type: 'scatter3d'
    };
    
    var obj4 = {
        x:unpack(rows, 'x4'), y: unpack(rows, 'y4'), z: unpack(rows, 'z4'), file: unpack(rows,'f4'),
        mode: 'markers',
        marker: {
            color: 'rgb(255, 255, 0)',
            size: 1,
            symbol: 'circle',
            line: {
            color: 'rgb(255, 255, 0)',
            width: 1},
            opacity: 0.8},
        name: 'C_id_3',
        type: 'scatter3d'};

        var obj5 = {
            x:unpack(rows, 'x5'), y: unpack(rows, 'y5'), z: unpack(rows, 'z5'), file: unpack(rows,'f5'),
            mode: 'markers',
            marker: {
                color: 'rgb(0, 255, 255)',
                size: 1,
                symbol: 'circle',
                line: {
                color: 'rgb(0, 255, 255)',
                width: 1},
                opacity: 0.8},
            name: 'C_id_4',
            type: 'scatter3d'};

    var myPlot = document.getElementById('myDiv'),
        data = [obj1, obj2, obj3, obj4, obj5],
        layout = {
            scene: {
                xaxis: {
                    title: 'f1',
                },
                yaxis: {
                    title: 'f2'
                },
                zaxis: {
                    title: 'f3'
                }
              },
            margin: {
    	    showlegend: true,
	            l: 0,
	            r: 0,
	            b: 0,
	            t: 15
            },
            // paper_bgcolor:'rgba(0.85,0.97,0.85,1)',
            // plot_bgcolor: 'rgba(0.85,0.93,0.85,1)',
        };

    Plotly.newPlot('myDiv', data, layout);
    myPlot.on('plotly_click', function(data){
        document.getElementById("filename").value="";
        console.log(data);
        fname=data.points[0].data.file[data.points[0].pointNumber];
        document.getElementById("altfile").value=fname;
        document.getElementById('span').innerHTML = "You have chosen " + document.getElementById("altfile").value +" file choose any option";
    });
});

Plotly.d3.csv('../new2d.csv', function(err, rows){
    function unpack(rows, key) {
        return rows.map(function(row)
        { return row[key]; });}
    
    var obj1 = {
        x:unpack(rows, 'x1'), y: unpack(rows, 'y1'), file: unpack(rows, 'f1'), 
        mode: 'markers',
        marker: {
            color: 'rgb(255, 0, 0)',
            size: 3,
            line: {
                color: 'rgb(255, 0, 0)',
            width: 0.5},
            opacity: 0.8},
        name: 'C_id_0',
        type: 'scatter',
    };
    
    var obj2 = {
        x:unpack(rows, 'x2'), y: unpack(rows, 'y2'), file: unpack(rows, 'f2'),
        mode: 'markers',
        marker: {
            color: 'rgb(0, 255, 0)',
            size: 3,
            line: {
                color: 'rgb(0, 255, 0)',
            width: 0.5},
            opacity: 0.8},
        name: 'C_id_1',
        type: 'scatter'
    };
    
    var obj3 = {
        x:unpack(rows, 'x3'), y: unpack(rows, 'y3'), file: unpack(rows, 'f3'),
        mode: 'markers',
        marker: {
            color: 'rgb(0, 0, 255)',
            size: 3,
            line: {
                color: 'rgb(0, 0, 255)',
            width: 0.5},
            opacity: 0.8},
        name: 'C_id_2',
        type: 'scatter'
    };
    
    var obj4 = {
        x:unpack(rows, 'x4'), y: unpack(rows, 'y4'), file: unpack(rows, 'f4'),
        mode: 'markers',
        marker: {
            color: 'rgb(255, 255, 0)',
            size: 3,
            symbol: 'circle',
            line: {
            color: 'rgb(255, 255, 0)',
            width: 1},
            opacity: 0.8},
        name: 'C_id_3',
        type: 'scatter'};

        var obj5 = {
            x:unpack(rows, 'x5'), y: unpack(rows, 'y5'), file: unpack(rows, 'f5'),
            mode: 'markers',
            marker: {
                color: 'rgb(0, 255, 255)',
                size: 3,
                symbol: 'circle',
                line: {
                color: 'rgb(0, 255, 255)',
                width: 1},
                opacity: 0.8},
            name: 'C_id_4',
            type: 'scatter'};

    var myPlot2 = document.getElementById('myDiv2'),
    data = [obj1, obj2, obj3, obj4, obj5],
    layout = {
        hovermode:'closest',
        margin: {
        showlegend: true,
	        l: 0,
	        r: 0,
	        b: 0,
	        t: 15
        },
        // paper_bgcolor:'rgba(0.88,0.88,0.95,1)',
        // plot_bgcolor: 'rgba(0.88,0.88,0.95,1)',
    };
    Plotly.newPlot('myDiv2', data, layout);
    myPlot2.on('plotly_click', function(data){
        document.getElementById("filename").value="";
        fname=data.points[0].data.file[data.points[0].pointIndex];
        console.log(fname);
        document.getElementById("altfile").value=fname;
        document.getElementById('span').innerHTML = "You have chosen " + document.getElementById("altfile").value +" file choose any option";
    });
});


