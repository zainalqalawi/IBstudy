class Application {
    constructor(){

    }

    input(){
        var subjects = [a,b,c,d,e,f];
        var time = int(t);
        var week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thurday", "Friday", "Saturday"];
        var part_time = 0;
        var sbj=[];
        var i = 0;
        var j = 0;
    }

    maker(){

        if (time > 2 || time == 2){
            part_time = time/3;
            i = 3;
        }
        else if (time < 2 && time > 0){
            part_time = time/2;
            i = 2;
        } else {
            print('out of bounds');
            part_time = part_time * 60;
        }
        var n,
        var randomIndex = Math.floor(Math.random()*textArray.length);
        for (n = 0; n <= week.length; n++){
            if (i == 3){
                print(week[j]);
                print(subjects[randomIndex]);
                print(subjects[randomIndex]);
                print(subjects[randomIndex]);
                j =+ 1;
            }
                
            else if (i == 2){
                print(week[j]);
                print(subjects[randomIndex]);
                print(subjects[randomIndex]);
                j =+ 1;
            }
                
            else{
                break;
            }
        }
    }
}
