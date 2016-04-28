function change_heading() {
	$("#Course Chart").
	console.log("what");
}
function sem_list()
{
    var selectedAnswer = document.getElementById("semester");
    var course_counts = get_course_counts();
    if (selectedAnswer != null)
    {
        var list = course_counts.search_by_semester(selectedAnswer);
        return list;
    }
    else
    {
        return course_counts;
    }
}

function get_semester(list)
{
    var ans_list;
    for(i=0; i<list.size(); i++)
    {
        ans_list.append(list[i].semester);
    }
    return ans_list;
}