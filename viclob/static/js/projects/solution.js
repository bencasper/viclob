$(function(){
	// 基于准备好的dom，初始化echarts实例
    var myChart01 = echarts.init(document.getElementById('chart01'));
    // 指定图表的配置项和数据
    var option01 = {
        backgroundColor: '#fff',
        title: {
            text: ''
        },
        tooltip: {},
        legend: {
            data:['播放量']
        },
        xAxis: {
            data: ["7-31","8-31","9-31","10-31","11-31","12-31"]
        },
        yAxis: {},
        series: [{
            name: '播放量',
            type: 'bar',
            data: [200000, 260000, 360000, 400000, 300000, 290000]
        }]
    };
    myChart01.setOption(option01);

    // pie
    var myChart02 = echarts.init(document.getElementById('chart02'));
    var option02 = {
          backgroundColor:'#fff',
          title: {
              text: '播放区域',
              left: 'center',
              textStyle: {
                  color: '#666'
              }
          },

          tooltip : {
              trigger: 'item',
              formatter: "{a} <br/>{b} : {c} ({d}%)"
          },
          // legend: {
          //     x: "left",
          //     data: ["北京", "上海", "广州", "深圳", "其它"]
          // },
          labelLine: {
              normal: {
                  smooth: .6
              }
          },
          calculable: !0,
          series: [{
              name: "",
              type: "pie",
              roseType: "area",
              label: {
                  normal: {
                      show: !0
                  },
                  emphasis: {
                      show: !0
                  }
              },
              lableLine: {
                  normal: {
                      show: !0
                  },
                  emphasis: {
                      show: !0
                  }
              },
              data: [{
                  value: 3050000,
                  name: "北京"
              }, {
                  value: 2340000,
                  name: "上海"
              }, {
                  value: 2450000,
                  name: "广州"
              }, {
                  value: 3450000,
                  name: "深圳"
              }, {
                  value: 1950000,
                  name: "其它"
              }]
          }]
	};
    myChart02.setOption(option02);


    // 折线图
    var myChart03 = echarts.init(document.getElementById('chart03'));
    // 指定图表的配置项和数据
    var option03 = {
        backgroundColor: '#fff',
	    title: {
	        text: '访问量',
	        subtext: ''
	    },
	    tooltip: {
	        trigger: 'axis'
	    },
	    legend: {
              x: "right",
	        data:['最高访问量','最低播访问量']
	    },
	    xAxis:  {
	        type: 'category',
	        boundaryGap: false,
	        data: ['周一','周二','周三','周四','周五','周六','周日']
	    },
	    yAxis: {
	        type: 'value',
	        axisLabel: {
	            formatter: '{value} 万次'
	        }
	    },
	    series: [
	        {
	            name:'最高访问量',
	            type:'line',
	            data:[11, 11, 15, 13, 12, 13, 10],
	            markPoint: {
	                data: [
	                    {type: 'max', name: '最大值'},
	                    {type: 'min', name: '最小值'}
	                ]
	            },
	            markLine: {
	                data: [
	                    {type: 'average', name: '平均值'}
	                ]
	            }
	        },
	        {
	            name:'最低播访问量',
	            type:'line',
	            data:[1, 1.3, 2, 5, 3, 2, 0],
	            markPoint: {
	                data: [
	                    {name: '周最低', value: 2, xAxis: 1, yAxis: 1.5}
	                ]
	            },
	            markLine: {
	                data: [
	                    {type: 'average', name: '平均值'},
	                    [{
	                        symbol: 'none',
	                        x: '90%',
	                        yAxis: 'max'
	                    }, {
	                        symbol: 'circle',
	                        label: {
	                            normal: {
	                                position: 'start',
	                                formatter: '最大值'
	                            }
	                        },
	                        type: 'max',
	                        name: '最高点'
	                    }]
	                ]
	            }
	        }
	    ]
    };

    // 使用刚指定的配置项和数据显示图表。
    myChart03.setOption(option03);

    // map
    var myChart04 = echarts.init(document.getElementById('chart04'));
        var geoCoordMap = {
    "海门":[121.15,31.89],
    "鄂尔多斯":[109.781327,39.608266],
    "招远":[120.38,37.35],
    "舟山":[122.207216,29.985295],
    "齐齐哈尔":[123.97,47.33],
    "盐城":[120.13,33.38],
    "赤峰":[118.87,42.28],
    "青岛":[120.33,36.07],
    "乳山":[121.52,36.89],
    "金昌":[102.188043,38.520089],
    "泉州":[118.58,24.93],
    "莱西":[120.53,36.86],
    "日照":[119.46,35.42],
    "胶南":[119.97,35.88],
    "南通":[121.05,32.08],
    "拉萨":[91.11,29.97],
    "云浮":[112.02,22.93],
    "梅州":[116.1,24.55],
    "文登":[122.05,37.2],
    "上海":[121.48,31.22],
    "攀枝花":[101.718637,26.582347],
    "威海":[122.1,37.5],
    "承德":[117.93,40.97],
    "厦门":[118.1,24.46],
    "汕尾":[115.375279,22.786211],
    "潮州":[116.63,23.68],
    "丹东":[124.37,40.13],
    "太仓":[121.1,31.45],
    "曲靖":[103.79,25.51],
    "烟台":[121.39,37.52],
    "福州":[119.3,26.08],
    "瓦房店":[121.979603,39.627114],
    "即墨":[120.45,36.38],
    "抚顺":[123.97,41.97],
    "玉溪":[102.52,24.35],
    "张家口":[114.87,40.82],
    "阳泉":[113.57,37.85],
    "莱州":[119.942327,37.177017],
    "湖州":[120.1,30.86],
    "汕头":[116.69,23.39],
    "昆山":[120.95,31.39],
    "宁波":[121.56,29.86],
    "湛江":[110.359377,21.270708],
    "揭阳":[116.35,23.55],
    "荣成":[122.41,37.16],
    "连云港":[119.16,34.59],
    "葫芦岛":[120.836932,40.711052],
    "常熟":[120.74,31.64],
    "东莞":[113.75,23.04],
    "河源":[114.68,23.73],
    "淮安":[119.15,33.5],
    "泰州":[119.9,32.49],
    "南宁":[108.33,22.84],
    "营口":[122.18,40.65],
    "惠州":[114.4,23.09],
    "江阴":[120.26,31.91],
    "蓬莱":[120.75,37.8],
    "韶关":[113.62,24.84],
    "嘉峪关":[98.289152,39.77313],
    "广州":[113.23,23.16],
    "延安":[109.47,36.6],
    "太原":[112.53,37.87],
    "清远":[113.01,23.7],
    "中山":[113.38,22.52],
    "昆明":[102.73,25.04],
    "寿光":[118.73,36.86],
    "盘锦":[122.070714,41.119997],
    "长治":[113.08,36.18],
    "深圳":[114.07,22.62],
    "珠海":[113.52,22.3],
    "宿迁":[118.3,33.96],
    "咸阳":[108.72,34.36],
    "铜川":[109.11,35.09],
    "平度":[119.97,36.77],
    "佛山":[113.11,23.05],
    "海口":[110.35,20.02],
    "江门":[113.06,22.61],
    "章丘":[117.53,36.72],
    "肇庆":[112.44,23.05],
    "大连":[121.62,38.92],
    "临汾":[111.5,36.08],
    "吴江":[120.63,31.16],
    "石嘴山":[106.39,39.04],
    "沈阳":[123.38,41.8],
    "苏州":[120.62,31.32],
    "茂名":[110.88,21.68],
    "嘉兴":[120.76,30.77],
    "长春":[125.35,43.88],
    "胶州":[120.03336,36.264622],
    "银川":[106.27,38.47],
    "张家港":[120.555821,31.875428],
    "三门峡":[111.19,34.76],
    "锦州":[121.15,41.13],
    "南昌":[115.89,28.68],
    "柳州":[109.4,24.33],
    "三亚":[109.511909,18.252847],
    "自贡":[104.778442,29.33903],
    "吉林":[126.57,43.87],
    "阳江":[111.95,21.85],
    "泸州":[105.39,28.91],
    "西宁":[101.74,36.56],
    "宜宾":[104.56,29.77],
    "呼和浩特":[111.65,40.82],
    "成都":[104.06,30.67],
    "大同":[113.3,40.12],
    "镇江":[119.44,32.2],
    "桂林":[110.28,25.29],
    "张家界":[110.479191,29.117096],
    "宜兴":[119.82,31.36],
    "北海":[109.12,21.49],
    "西安":[108.95,34.27],
    "金坛":[119.56,31.74],
    "东营":[118.49,37.46],
    "牡丹江":[129.58,44.6],
    "遵义":[106.9,27.7],
    "绍兴":[120.58,30.01],
    "扬州":[119.42,32.39],
    "常州":[119.95,31.79],
    "潍坊":[119.1,36.62],
    "重庆":[106.54,29.59],
    "台州":[121.420757,28.656386],
    "南京":[118.78,32.04],
    "滨州":[118.03,37.36],
    "贵阳":[106.71,26.57],
    "无锡":[120.29,31.59],
    "本溪":[123.73,41.3],
    "克拉玛依":[84.77,45.59],
    "渭南":[109.5,34.52],
    "马鞍山":[118.48,31.56],
    "宝鸡":[107.15,34.38],
    "焦作":[113.21,35.24],
    "句容":[119.16,31.95],
    "北京":[116.46,39.92],
    "徐州":[117.2,34.26],
    "衡水":[115.72,37.72],
    "包头":[110,40.58],
    "绵阳":[104.73,31.48],
    "乌鲁木齐":[87.68,43.77],
    "枣庄":[117.57,34.86],
    "杭州":[120.19,30.26],
    "淄博":[118.05,36.78],
    "鞍山":[122.85,41.12],
    "溧阳":[119.48,31.43],
    "库尔勒":[86.06,41.68],
    "安阳":[114.35,36.1],
    "开封":[114.35,34.79],
    "济南":[117,36.65],
    "德阳":[104.37,31.13],
    "温州":[120.65,28.01],
    "九江":[115.97,29.71],
    "邯郸":[114.47,36.6],
    "临安":[119.72,30.23],
    "兰州":[103.73,36.03],
    "沧州":[116.83,38.33],
    "临沂":[118.35,35.05],
    "南充":[106.110698,30.837793],
    "天津":[117.2,39.13],
    "富阳":[119.95,30.07],
    "泰安":[117.13,36.18],
    "诸暨":[120.23,29.71],
    "郑州":[113.65,34.76],
    "哈尔滨":[126.63,45.75],
    "聊城":[115.97,36.45],
    "芜湖":[118.38,31.33],
    "唐山":[118.02,39.63],
    "平顶山":[113.29,33.75],
    "邢台":[114.48,37.05],
    "德州":[116.29,37.45],
    "济宁":[116.59,35.38],
    "荆州":[112.239741,30.335165],
    "宜昌":[111.3,30.7],
    "义乌":[120.06,29.32],
    "丽水":[119.92,28.45],
    "洛阳":[112.44,34.7],
    "秦皇岛":[119.57,39.95],
    "株洲":[113.16,27.83],
    "石家庄":[114.48,38.03],
    "莱芜":[117.67,36.19],
    "常德":[111.69,29.05],
    "保定":[115.48,38.85],
    "湘潭":[112.91,27.87],
    "金华":[119.64,29.12],
    "岳阳":[113.09,29.37],
    "长沙":[113,28.21],
    "衢州":[118.88,28.97],
    "廊坊":[116.7,39.53],
    "菏泽":[115.480656,35.23375],
    "合肥":[117.27,31.86],
    "武汉":[114.31,30.52],
    "大庆":[125.03,46.58]
};

var convertData = function (data) {
    var res = [];
    for (var i = 0; i < data.length; i++) {
        var geoCoord = geoCoordMap[data[i].name];
        if (geoCoord) {
            res.push({
                name: data[i].name,
                value: geoCoord.concat(data[i].value)
            });
        }
    }
    return res;
};

option04 = {
    backgroundColor: '#fff',
    title: {
        text: '播放量分布',
        x:'center',
        textStyle: {
            color: '#666'
        }
    },
    tooltip: {
        trigger: 'item',
        formatter: function (params) {
            return params.name + ' : ' + params.value[2];
        }
    },
    legend: {
        orient: 'vertical',
        y: 'bottom',
        x:'right',
        data:['播放量'],
        textStyle: {
            color: '#333'
        }
    },
    visualMap: {
        min: 0,
        max: 3000000,
        calculable: true,
        itemWidth: 10,
        itemHeight: 80,
        inRange: {
            color: ['#ffc7cb','#fb6873', '#c23531']  //等级颜色区分
        },
        textStyle: {
            color: '#666',
        }
    },
    geo: {
        map: 'china',
        label: {
            emphasis: {
                show: false
            }
        },
        itemStyle: {
            normal: {
                areaColor: '#f6f6f6',
                borderColor: '#111'
            },
            emphasis: {
                areaColor: '#efefef'
            }
        }
    },
    series: [
        {
            name: '播放分布',
            type: 'scatter',
            coordinateSystem: 'geo',
            data: convertData([
                {name: "海门", value: 90000},
                {name: "鄂尔多斯", value: 120000},
                {name: "招远", value: 120000},
                {name: "舟山", value: 120000},
                {name: "齐齐哈尔", value: 140000},
                {name: "盐城", value: 150000},
                {name: "赤峰", value: 160000},
                {name: "青岛", value: 180000},
                {name: "乳山", value: 180000},
                {name: "金昌", value: 190000},
                {name: "泉州", value: 210000},
                {name: "莱西", value: 210000},
                {name: "日照", value: 210000},
                {name: "胶南", value: 220000},
                {name: "南通", value: 230000},
                {name: "拉萨", value: 240000},
                {name: "云浮", value: 240000},
                {name: "梅州", value: 250000},
                {name: "文登", value: 250000},
                {name: "上海", value: 250000},
                {name: "攀枝花", value: 250000},
                {name: "威海", value: 250000},
                {name: "承德", value: 250000},
                {name: "厦门", value: 260000},
                {name: "汕尾", value: 260000},
                {name: "潮州", value: 260000},
                {name: "丹东", value: 270000},
                {name: "太仓", value: 270000},
                {name: "曲靖", value: 270000},
                {name: "烟台", value: 280000},
                {name: "福州", value: 290000},
                {name: "瓦房店", value: 300000},
                {name: "即墨", value: 300000},
                {name: "抚顺", value: 310000},
                {name: "玉溪", value: 310000},
                {name: "张家口", value: 310000},
                {name: "阳泉", value: 310000},
                {name: "莱州", value: 320000},
                {name: "湖州", value: 320000},
                {name: "汕头", value: 320000},
                {name: "昆山", value: 330000},
                {name: "宁波", value: 330000},
                {name: "湛江", value: 330000},
                {name: "揭阳", value: 340000},
                {name: "荣成", value: 340000},
                {name: "连云港", value: 350000},
                {name: "葫芦岛", value: 350000},
                {name: "常熟", value: 360000},
                {name: "东莞", value: 360000},
                {name: "河源", value: 360000},
                {name: "淮安", value: 360000},
                {name: "泰州", value: 360000},
                {name: "南宁", value: 370000},
                {name: "营口", value: 370000},
                {name: "惠州", value: 370000},
                {name: "江阴", value: 370000},
                {name: "蓬莱", value: 370000},
                {name: "韶关", value: 380000},
                {name: "嘉峪关", value: 380000},
                {name: "广州", value: 380000},
                {name: "延安", value: 380000},
                {name: "太原", value: 390000},
                {name: "清远", value: 390000},
                {name: "中山", value: 390000},
                {name: "昆明", value: 390000},
                {name: "寿光", value: 400000},
                {name: "盘锦", value: 400000},
                {name: "长治", value: 410000},
                {name: "深圳", value: 410000},
                {name: "珠海", value: 420000},
                {name: "宿迁", value: 430000},
                {name: "咸阳", value: 430000},
                {name: "铜川", value: 440000},
                {name: "平度", value: 440000},
                {name: "佛山", value: 440000},
                {name: "海口", value: 440000},
                {name: "江门", value: 450000},
                {name: "章丘", value: 450000},
                {name: "肇庆", value: 460000},
                {name: "大连", value: 470000},
                {name: "临汾", value: 470000},
                {name: "吴江", value: 470000},
                {name: "石嘴山", value: 490000},
                {name: "沈阳", value: 500000},
                {name: "苏州", value: 500000},
                {name: "茂名", value: 500000},
                {name: "嘉兴", value: 510000},
                {name: "长春", value: 510000},
                {name: "胶州", value: 520000},
                {name: "银川", value: 520000},
                {name: "张家港", value: 520000},
                {name: "三门峡", value: 530000},
                {name: "锦州", value: 540000},
                {name: "南昌", value: 540000},
                {name: "柳州", value: 540000},
                {name: "三亚", value: 540000},
                {name: "自贡", value: 560000},
                {name: "吉林", value: 560000},
                {name: "阳江", value: 570000},
                {name: "泸州", value: 570000},
                {name: "西宁", value: 570000},
                {name: "宜宾", value: 580000},
                {name: "呼和浩特", value: 580000},
                {name: "成都", value: 580000},
                {name: "大同", value: 580000},
                {name: "镇江", value: 590000},
                {name: "桂林", value: 590000},
                {name: "张家界", value: 590000},
                {name: "宜兴", value: 590000},
                {name: "北海", value: 600000},
                {name: "西安", value: 610000},
                {name: "金坛", value: 620000},
                {name: "东营", value: 620000},
                {name: "牡丹江", value: 630000},
                {name: "遵义", value: 630000},
                {name: "绍兴", value: 630000},
                {name: "扬州", value: 640000},
                {name: "常州", value: 640000},
                {name: "潍坊", value: 650000},
                {name: "重庆", value: 660000},
                {name: "台州", value: 600007},
                {name: "南京", value: 600007},
                {name: "滨州", value: 700000},
                {name: "贵阳", value: 700001},
                {name: "无锡", value: 710000},
                {name: "本溪", value: 710000},
                {name: "克拉玛依", value: 720000},
                {name: "渭南", value: 700002},
                {name: "马鞍山", value: 700002},
                {name: "宝鸡", value: 700002},
                {name: "焦作", value: 700005},
                {name: "句容", value: 700005},
                {name: "北京", value: 700009},
                {name: "徐州", value: 700009},
                {name: "衡水", value: 800000},
                {name: "包头", value: 800000},
                {name: "绵阳", value: 8000000000},
                {name: "乌鲁木齐", value: 800004},
                {name: "枣庄", value: 800004},
                {name: "杭州", value: 800004},
                {name: "淄博", value: 800005},
                {name: "鞍山", value: 800006},
                {name: "溧阳", value: 800006},
                {name: "库尔勒", value: 860000},
                {name: "安阳", value: 900000},
                {name: "开封", value: 900000},
                {name: "济南", value: 900002},
                {name: "德阳", value: 900003},
                {name: "温州", value: 900005},
                {name: "九江", value: 900006},
                {name: "邯郸", value: 900008},
                {name: "临安", value: 900009},
                {name: "兰州", value: 900009},
                {name: "沧州", value: 1000000},
                {name: "临沂", value: 1030000},
                {name: "南充", value: 1040000},
                {name: "天津", value: 1000005},
                {name: "富阳", value: 1000006},
                {name: "泰安", value: 1100002},
                {name: "诸暨", value: 1000012},
                {name: "郑州", value: 1000013},
                {name: "哈尔滨", value: 1000014},
                {name: "聊城", value: 1000016},
                {name: "芜湖", value: 1170000},
                {name: "唐山", value: 1190000},
                {name: "平顶山", value: 1190000},
                {name: "邢台", value: 1190000},
                {name: "德州", value: 1200000},
                {name: "济宁", value: 1200000},
                {name: "荆州", value: 1270000},
                {name: "宜昌", value: 1300000},
                {name: "义乌", value: 1320000},
                {name: "丽水", value: 1330000},
                {name: "洛阳", value: 1340000},
                {name: "秦皇岛", value: 1360000},
                {name: "株洲", value: 1430000},
                {name: "石家庄", value: 1470000},
                {name: "莱芜", value: 1480000},
                {name: "常德", value: 1520000},
                {name: "保定", value: 1530000},
                {name: "湘潭", value: 1540000},
                {name: "金华", value: 1570000},
                {name: "岳阳", value: 1690000},
                {name: "长沙", value: 1750000},
                {name: "衢州", value: 1770000},
                {name: "廊坊", value: 1930000},
                {name: "菏泽", value: 1940000},
                {name: "合肥", value: 2290000},
                {name: "武汉", value: 2730000},
                {name: "大庆", value: 2790000}
            ]),
            symbolSize: 12,
            label: {
                normal: {
                    show: false
                },
                emphasis: {
                    show: false
                }
            },
            itemStyle: {
                emphasis: {
                    borderColor: '#fff',
                    borderWidth: 1
                }
            }
        }
    ]
}
        myChart04.setOption(option04);

        $(".net").bubbler(
            {
                color: "#ea734b",
                ammount: "60",
                min: "0.05",
                max: "0.2",
                time: "20",
            }
        );
        var myChart = echarts.init(document.getElementById('main'));
    // 指定图表的配置项和数据
    var option = {
        tooltip : {
            show : true,   //默认显示
            showContent:true, //是否显示提示框浮层
            trigger:'item',//触发类型，默认数据项触发
            triggerOn:'click',//提示触发条件，mousemove鼠标移至触发，还有click点击触发
            alwaysShowContent:false, //默认离开提示框区域隐藏，true为一直显示
            showDelay:0,//浮层显示的延迟，单位为 ms，默认没有延迟，也不建议设置。在 triggerOn 为 'mousemove' 时有效。
            hideDelay:200,//浮层隐藏的延迟，单位为 ms，在 alwaysShowContent 为 true 的时候无效。
            enterable:false,//鼠标是否可进入提示框浮层中，默认为false，如需详情内交互，如添加链接，按钮，可设置为 true。
            position:'right',//提示框浮层的位置，默认不设置时位置会跟随鼠标的位置。只在 trigger 为'item'的时候有效。
            confine:false,//是否将 tooltip 框限制在图表的区域内。外层的 dom 被设置为 'overflow: hidden'，或者移动端窄屏，导致 tooltip 超出外界被截断时，此配置比较有用。
            transitionDuration:0.4,//提示框浮层的移动动画过渡时间，单位是 s，设置为 0 的时候会紧跟着鼠标移动。
        },
        series : [ {
            type : 'graph', //关系图
            name : "", //系列名称，用于tooltip的显示，legend 的图例筛选，在 setOption 更新数据和配置项时用于指定对应的系列。
            layout : 'force', //图的布局，类型为力导图，'circular' 采用环形布局，见示例 Les Miserables
            legendHoverLink : true,//是否启用图例 hover(悬停) 时的联动高亮。
            hoverAnimation : true,//是否开启鼠标悬停节点的显示动画
            coordinateSystem : null,//坐标系可选
            xAxisIndex : 0, //x轴坐标 有多种坐标系轴坐标选项
            yAxisIndex : 0, //y轴坐标 
            force : { //力引导图基本配置
                //initLayout: ,//力引导的初始化布局，默认使用xy轴的标点
                repulsion : 100,//节点之间的斥力因子。支持数组表达斥力范围，值越大斥力越大。
                gravity : 0.08,//节点受到的向中心的引力因子。该值越大节点越往中心点靠拢。
                edgeLength :120,//边的两个节点之间的距离，这个距离也会受 repulsion。[10, 50] 。值越小则长度越长
                layoutAnimation : true
            //因为力引导布局会在多次迭代后才会稳定，这个参数决定是否显示布局的迭代动画，在浏览器端节点数据较多（>100）的时候不建议关闭，布局过程会造成浏览器假死。                        
            },
            roam : false,//是否开启鼠标缩放和平移漫游。默认不开启。如果只想要开启缩放或者平移，可以设置成 'scale' 或者 'move'。设置成 true 为都开启
            nodeScaleRatio :0,//鼠标漫游缩放时节点的相应缩放比例，当设为0时节点不随着鼠标的缩放而缩放
            draggable : true,//节点是否可拖拽，只在使用力引导布局的时候有用。
            focusNodeAdjacency : true,//是否在鼠标移到节点上的时候突出显示节点以及节点的边和邻接节点。
            //symbol:'roundRect',//关系图节点标记的图形。ECharts 提供的标记类型包括 'circle'(圆形), 'rect'（矩形）, 'roundRect'（圆角矩形）, 'triangle'（三角形）, 'diamond'（菱形）, 'pin'（大头针）, 'arrow'（箭头）  也可以通过 'image://http://www.viclob.com/static/url' 设置为图片，其中 url 为图片的链接。'path:// 这种方式可以任意改变颜色并且抗锯齿
            //symbolSize:10 ,//也可以用数组分开表示宽和高，例如 [20, 10] 如果需要每个数据的图形大小不一样，可以设置为如下格式的回调函数：(value: Array|number, params: Object) => number|Array
            //symbolRotate:,//关系图节点标记的旋转角度。注意在 markLine 中当 symbol 为 'arrow' 时会忽略 symbolRotate 强制设置为切线的角度。
            //symbolOffset:[0,0],//关系图节点标记相对于原本位置的偏移。[0, '50%']
            //edgeSymbol : [ 'none', 'none' ],
            edgeSymbol: ['circle', 'arrow'],//边两端的标记类型，可以是一个数组分别指定两端，也可以是单个统一指定。默认不显示标记，常见的可以设置为箭头，如下：edgeSymbol: ['circle', 'arrow']
            edgeSymbolSize : 1,//边两端的标记大小，可以是一个数组分别指定两端，也可以是单个统一指定。
            itemStyle : {//===============图形样式，有 normal 和 emphasis 两个状态。normal 是图形在默认状态下的样式；emphasis 是图形在高亮状态下的样式，比如在鼠标悬浮或者图例联动高亮时。
                normal : { //默认样式
                    label : {
                        show : true
                    },
                    borderType : 'solid', //图形描边类型，默认为实线，支持 'solid'（实线）, 'dashed'(虚线), 'dotted'（点线）。
                    borderColor : 'rgba(255,255,255,0.8)', //设置图形边框为淡金色,透明度为0.4
                    borderWidth : 4, //图形的描边线宽。为 0 时无描边。
                    opacity : 1
                // 图形透明度。支持从 0 到 1 的数字，为 0 时不绘制该图形。默认0.5

                },
                emphasis : {//高亮状态

                }
            },
            lineStyle : { //==========关系边的公用线条样式。
                normal : {
                    color : 'rgba(255,255,255,0.8)',
                    width : '1',
                    type : 'dotted', //线的类型 'solid'（实线）'dashed'（虚线）'dotted'（点线）
                    curveness : 0.3, //线条的曲线程度，从0到1
                    opacity : 1
                // 图形透明度。支持从 0 到 1 的数字，为 0 时不绘制该图形。默认0.5
                },
                emphasis : {//高亮状态

                }
            },
            label : { //=============图形上的文本标签
                normal : {
                    show : true,//是否显示标签。
                    position : 'inside',//标签的位置。['50%', '50%'] [x,y]
                    textStyle : { //标签的字体样式
                        color : '#fff', //字体颜色
                        fontStyle : 'normal',//文字字体的风格 'normal'标准 'italic'斜体 'oblique' 倾斜
                        fontWeight : 'normal',//'normal'标准'bold'粗的'bolder'更粗的'lighter'更细的或100 | 200 | 300 | 400...
                        fontFamily : 'sans-serif', //文字的字体系列
                        fontSize : 12, //字体大小
                    }
                },
                emphasis : {//高亮状态

                }
            },
            edgeLabel : {//==============线条的边缘标签 
                normal : {
                    show : false
                },
                emphasis : {//高亮状态

                }
            },
            //别名为nodes   name:影响图形标签显示,value:影响选中后值得显示,category:所在类目的index,symbol:类目节点标记图形,symbolSize:10图形大小
            //label:标签样式。
            data : [{
                id : 0,
                category :0,
                name : '用户',
                symbol : 'circle',
                value : 20,
                symbolSize : 90
            },{
                id : 1,
                category : 1,
                name : '视频app',
                symbol : 'circle',
                value : 20,
                symbolSize : 90
            },{
                id : 2,
                category : 1,
                name : '社群',
                symbol : 'circle',
                value : 20,
                symbolSize : 90
            },{
                id : 3,
                category : 1,
                name :  '互联网电视',
                symbol : 'circle',
                value : 20,
                symbolSize : 90
            },{
                id : 4,
                category : 1,
                name : '视频网站',
                symbol : 'circle',
                value : 20,
                symbolSize : 90
            },{
                id : 5,
                category : 1,
                name : '移动新媒体',
                symbol : 'circle',
                value : 20,
                symbolSize : 90
            },{
                id : 6,
                category : 1,
                name : '自媒体群',
                symbol : 'circle',
                value : 20,
                symbolSize : 90
            },{
                id : 7,
                category : 1,
                name : '',
                symbol : 'image://http://www.viclob.com/static/http://www.viclob.com/static/images/map/app/app-56.png',
                value : 20,
                symbolSize : 80
            }, {
                id : 8,
                category : 1,
                name : '',
                symbol : 'image://http://www.viclob.com/static/http://www.viclob.com/static/images/map/app/app-acfun.png',
                value : 20,
                symbolSize : 70
            }, {
                id : 9,
                category : 1,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/app/app-bilibili.png',
                value : 20,
                symbolSize : 90
            }, {
                id : 10,
                category : 1,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/app/app-meipai.png',
                value : 20,
                symbolSize : 80
            }, {
                id : 11,
                category : 1,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/app/app-miliao.png',
                value : 20,
                symbolSize : 70
            }, {
                id : 12,
                category : 1,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/app/app-xiangji.png',
                value : 20,
                symbolSize : 80
            }, {
                id : 13,
                category : 2,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/shequn/shequn-baidu.png',
                value : 20,
                symbolSize : 80
            }, {
                id : 14,
                category : 2,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/shequn/shequn-douban.png',
                value : 20,
                symbolSize : 60
            }, {
                id : 15,
                category : 2,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/shequn/shequn-jianshu.png',
                value : 20,
                symbolSize : 70
            }, {
                id : 16,
                category : 2,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/shequn/shequn-qzone.png',
                value : 20,
                symbolSize : 60
            }, {
                id : 17,
                category : 2,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/shequn/shequn-zhihu.png',
                value : 20,
                symbolSize : 80
            }, {
                id : 18,
                category : 3,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/tv/tv-haixing.png',
                value : 20,
                symbolSize : 90
            }, {
                id : 19,
                category : 3,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/tv/tv-huashu.png',
                value : 20,
                symbolSize : 80
            }, {
                id : 20,
                category : 3,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/tv/tv-letv.png',
                value : 20,
                symbolSize : 80
            }, {
                id : 21,
                category : 3,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/tv/tv-mangguo.png',
                value : 20,
                symbolSize : 70
            }, {
                id : 22,
                category : 3,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/tv/tv-weijing.png',
                value : 20,
                symbolSize : 90
            }, {
                id : 23,
                category : 3,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/tv/tv-xiaomi.png',
                value : 20,
                symbolSize : 70,
            }, {
                id : 24,
                category : 4,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/video/video-56.png',
                value : 20,
                symbolSize : 60,
            }, {
                id : 25,
                category : 4,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/video/video-iqi.png',
                value : 20,
                symbolSize : 70,
            }, {
                id : 26,
                category : 4,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/video/video-ku6.png',
                value : 20,
                symbolSize : 90,
            }, {
                id : 27,
                category : 4,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/video/video-leshi.png',
                value : 20,
                symbolSize : 70,
            }, {
                id : 28,
                category : 4,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/video/video-pps.png',
                value : 20,
                symbolSize : 80,
            },{
                id : 29,
                category : 4,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/video/video-souhu.png',
                value : 20,
                symbolSize : 70,
            },{
                id : 30,
                category : 4,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/video/video-tengxun.png',
                value : 20,
                symbolSize : 90,
            },{
                id : 31,
                category : 4,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/video/video-tudou.png',
                value : 20,
                symbolSize : 70,
            },{
                id : 32,
                category : 4,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/video/video-youku.png',
                value : 20,
                symbolSize : 80,
            },{
                id : 33,
                category : 1,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/wap/wap-baidu.png',
                value : 20,
                symbolSize : 70,
            },{
                id : 34,
                category : 1,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/wap/wap-sina.png',
                value : 20,
                symbolSize : 80,
            },{
                id : 35,
                category : 1,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/wap/wap-souhu.png',
                value : 20,
                symbolSize : 70,
            },{
                id : 36,
                category : 1,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/wap/wap-tengxun.png',
                value : 20,
                symbolSize : 90,
            },{
                id : 37,
                category : 1,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/wap/wap-wangyi.png',
                value : 20,
                symbolSize : 70,
            },{
                id : 38,
                category : 1,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/wap/wap-weixin.png',
                value : 20,
                symbolSize : 70,
            },{
                id : 39,
                category : 1,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/wap/wap-yidianzixun.png',
                value : 20,
                symbolSize : 90,
            },{
                id : 40,
                category : 1,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/wap/wap-youfa.png',
                value : 20,
                symbolSize : 70,
            },{
                id : 41,
                category : 2,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/zimei/zimei-baijia.png',
                value : 20,
                symbolSize : 90,
            },{
                id : 42,
                category : 2,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/zimei/zimei-bjtime.png',
                value : 20,
                symbolSize : 70,
            },{
                id : 43,
                category : 2,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/zimei/zimei-souhu.png',
                value : 20,
                symbolSize : 70,
            },{
                id : 44,
                category : 2,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/zimei/zimei-toutiao.png',
                value : 20,
                symbolSize : 90,
            },{
                id : 45,
                category : 2,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/zimei/zimei-uc.png',
                value : 46,
                symbolSize : 90,
            },{
                id : 46,
                category : 2,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/zimei/zimei-wangyi.png',
                value : 20,
                symbolSize : 70,
            },{
                id : 47,
                category : 2,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/zimei/zimei-weixin.png',
                value : 20,
                symbolSize : 70,
            },{
                id : 48,
                category : 2,
                name : '',
                symbol : 'image://http://www.viclob.com/static/images/map/zimei/zimei-yidianhao.png',
                value : 20,
                symbolSize : 90,
            }],
            categories : [ //symbol name：用于和 legend 对应以及格式化 tooltip 的内容。 label有效
            {
                name : '负载',
                symbol : 'rect',
                label : { //标签样式
                }
            }, {
                name : '中间件',
                symbol : 'rect'
            }, {
                name : '端口号',
                symbol : 'roundRect'
            }, {
                name : '数据库',
                symbol : 'roundRect'
            }, {
                name : '用户名',
                symbol : 'roundRect'
            } ],
            links : [ //edges是其别名代表节点间的关系数据。
            {
                source : 0,
                target : 1
            }, {
                source : 0,
                target : 2
            }, {
                source : 0,
                target : 3
            }, {
                source : 0,
                target : 4
            }, {
                source : 0,
                target : 5
            }, {
                source : 0,
                target : 6
            }, {
                source : 1,
                target : 7
            }, {
                source : 1,
                target : 8
            }, {
                source : 1,
                target : 9
            }, {
                source : 1,
                target : 10
            }, {
                source : 1,
                target : 11
            }, {
                source : 1,
                target : 12
            }, {
                source : 2,
                target : 13
            }, {
                source : 2,
                target : 14
            }, {
                source : 2,
                target : 15
            }, {
                source : 2,
                target : 16
            }, {
                source : 2,
                target : 17
            },{
                source : 3,
                target : 18
            },{
                source : 3,
                target : 19
            },{
                source : 3,
                target : 20
            },{
                source : 3,
                target : 21
            },{
                source : 3,
                target : 22
            },{
                source : 3,
                target : 23
            },{
                source : 4,
                target : 24
            },{
                source : 4,
                target : 25
            },{
                source : 4,
                target : 26
            },{
                source : 4,
                target : 27
            },{
                source : 4,
                target : 28
            },{
                source : 4,
                target : 29
            },{
                source : 4,
                target : 30
            },{
                source : 4,
                target : 31
            },{
                source : 4,
                target : 32
            },{
                source : 5,
                target : 33
            },{
                source : 5,
                target : 34
            },{
                source : 5,
                target : 35
            },{
                source : 5,
                target : 36
            },{
                source : 5,
                target : 37
            },{
                source : 5,
                target : 38
            },{
                source : 5,
                target : 39
            },{
                source : 5,
                target : 40
            },{
                source : 6,
                target : 41
            },{
                source : 6,
                target : 42
            },{
                source : 6,
                target : 43
            },{
                source : 6,
                target : 44
            },{
                source : 6,
                target : 45
            },{
                source : 6,
                target : 46
            },{
                source : 6,
                target : 47
            },{
                source : 6,
                target : 48
            }
            ]
        } ]
    };
    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
})