var zip;

function main(id) {
    //alert("lol");
    var $result = $("#result" + id);
    $result.html("<li><progress id=\"p\"></progress></li>");
    var fName = document.querySelector('[data-result-id="' + id + '"]').dataset.sourceUrl;
    $result.append('<input type="button" value="send" id="sendb" />');
    $hiddendiv = $('div[name=csrfmiddlewaretoken]');
    // var zip;


    var progressBar = $("#p"),
        client = new XMLHttpRequest();
    client.responseType = "arraybuffer";
    client.open("GET", fName, true);
    if (client.overrideMimeType) {
        client.overrideMimeType('text/plain; charset=x-user-defined');
    }
    client.onprogress = function(pe) {
        if (pe.lengthComputable) {
            progressBar.max = pe.total / pe.total;
            progressBar.value = pe.loaded / pe.total;
        }
    }


    client.onloadend = function(pe) {

        progressBar.value = pe.loaded;


        $.each($('[data-element]'), function() {
            $(this).on('mouseenter', function() {
                $('div', this).show();
                var parr = this;
                $('div', this).on('click', function() {
                    //console.log(zip.files);
                    zip.remove(this.id);
                    //console.log(zip.files);
                    console.log(this.id);
                    $(parr).hide();
                });
            }).on('mouseleave', function() {
                $('div', this).hide();
            });
        });
        var $sendb = $("#sendb");
        $sendb.on('click', function() {
            console.log("asd");
            var content = zip.generate();
            //location.href="data:application/zip;base64,"+content;
            content = content;
            //content = atob(content);
            //console.log(content);
            // console.log("data:application/zip;base64," + content);

            // // var blob = new Blob(content, "application/zip");

            // var form = new FormData();
            // form.append("file", content);S
            // var oReq = new XMLHttpRequest();
            // oReq.open("POST", "/theme/zip/type/");
            // oReq.setRequestHeader("Content-Type", "application/zip");
            // oReq.send(form);

            var data = new FormData();
            // Добавим в новую форму файл
            data.append('file', content);
            // console.log(typeof atob(content));
            data.append('csrfmiddlewaretoken', $('[name="csrfmiddlewaretoken"]')[0].value);
            data.append('theme_id', $('[name="theme_id"]')[0].innerText);
            // console.log('token ' + $(['[name="csrfmiddlewaretoken"]'])[0].value);
            // console.log(data);

            // Создадим асинхронный запрос
            $.ajax({
                // На какой URL будет послан запрос
                url: '/theme/zip/type/',
                // Тип запроса
                type: 'POST',
                // Какие данные нужно передать
                data: data,
                // Эта опция не разрешает jQuery изменять данные
                processData: false,
                // Эта опция не разрешает jQuery изменять типы данных
                contentType: false,
                // Формат данных ответа с сервера
                dataType: 'html',
                // Функция удачного ответа с сервера
                success: function(result) {
                     console.log(result);
                }
            });

            // $('#fileInput').value = content;
            // var fi = new FormData($('#fileInput'));
            // var message = '';

            // var options = {
            //     // enctype: 'multipart/form-data',
            //     processData: false,
            //     contentType: false,
            //     url: '/theme/zip/type/',
            //     type: 'POST',
            //     data: fi,
            //     //processData: true, // Don't process the files
            //     //contentType: true, // Set content type to false as jQuery will tell the server its a query string request

            //     error: function(response) {
            //         message = '<span class="error">We\'re sorry, but something went wrong. Retry.</span>';
            //         $('.upload-message').html(message);
            //         $('fileInput').val(content);
            //     },
            //     success: function(response) {
            //         message = '<span class="' + response.status + '">' + response.result + '</span> ';
            //         message = (response.status == 'success') ? message + response.fileLink : message;
            //         $('.upload-message').html(message);
            //         $('fileInput').val(content);
            //     }
            // };
            // $('#uploadForm').ajaxSubmit(options);

            //     $('#fileInput').val(content);
            //     var message = '';
            // var options = {
            //     url: '/theme/zip/type/',
            //     data: {
            //         file: "data:application/zip;base64," + content
            //     },
            //     error: function(response) {
            //         message = '<span class="error">We\'re sorry, but something went wrong. Retry.</span>';
            //         $('.upload-message').html(message);
            //         $('fileInput').val(content);
            //     },
            //     success: function(response) {
            //         message = '<span class="' + response.status + '">' + response.result + '</span> ';
            //         message = ( response.status == 'success' ) ? message + response.fileLink : message;
            //         $('.upload-message').html(message);
            //         $('fileInput').val(content);
            //     }
            // };
            // $('#uploadForm').ajaxSubmit(options);

        });
    }


    client.onreadystatechange = function(e) {
        if (this.readyState == 4 && this.status == 200) {
            // remove content
            // Closure to capture the file information.
            //$result.html("");

            var $title = $("<h3>", {
                text: fName
            });
            $result.append($title);
            var $ul = $("<ul>");
            try {

                zip = new JSZip(this.response, {
                    base64: false
                });


                // that, or a good ol' for(var entryName in zip.files)
                $images = $("<li>");
                $txts = $("<li>");
                $other = $("<li>");
                $.each(zip.files, function(index, zipEntry) {
                    if (zipEntry.name.search(".png") != -1) {
                        $images.append("<div class=\"col-md-5\" data-element=\"image\"> <p>" + zipEntry.name + "</p>" + createImageElement(zipEntry.asUint8Array(), "png", zipEntry.name) + "</div>");
                        //$images.append("<li data-element=\"image\">" + createImageElement(zipEntry.asUint8Array(), "png", zipEntry.name) + "</li>");

                    } else
                    if (zipEntry.name.search(".txt") != -1) {
                        $txts.append("<h4>" + zipEntry.name + "</h4>");
                        $txts.append('<p><textarea id="txtar' + zipEntry.id + '" rows="10" cols="45" name="text">' + zipEntry.asText() + '</textarea>');
                        $b1 = $('<p>');
                        $b2 = $('<input>', {
                            type: 'button',
                            value: 'save'
                        });
                        $b2.click(function() {
                            var nmtxt = zipEntry.name;
                            var fltxt = $("#txtar" + zipEntry.id)[0].value;
                            zip.remove(zipEntry.id);
                            zip.file(nmtxt, fltxt);
                        });
                        $b1.append($b2);
                        $txts.append($b1);
                    } else
                    if (zipEntry.asText()) {
                        $other.append("<h4>" + zipEntry.name + "</h4>");

                    }
                });
                // end of the magic !
            } catch (e) {
                $ul.append("<li class='error'>Error reading " + fName + " : " + e.message + "</li>");
                console.log(e.message);
            }

            // canvas.addEventListener('onclick', clickReporter, false);
            $ul.append($other);
            $ul.append($images);
            $ul.append($txts);
            $result.append($ul);


            //$sendb.onclick = sendToAdamchik.bind(zip);


        }
    };
    client.send();
}

function createImageElement(data, format, name) {


    var s = "",
        i = 0,
        l = data.length;
    while (i < l) {
        var end = Math.min(i + 10000, l);
        s += String.fromCharCode.apply(null, data.subarray(i, end));
        i = end;
    }
    return '<img  src="data:image/' + format + ';base64,' + btoa(s) + '"/><div class="delete-image" id="' + name + '">X</div>';
}