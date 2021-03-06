# -*- coding: utf-8 -*-
from mole_api import request, response, add_route, JTemplate, HTTPError, valid_user

@valid_user()
def AppPageFunc(app_label, model_name):
    '''
    Page页面
    '''
    from custom_model_view import AppPageView
    return AppPageView(request, app_label, model_name)
add_route(AppPageFunc, '/page/:app_label/:model_name/')

@valid_user()
def GridModelFunc(app_label, model_name):
    '''
    Grid数据
    '''
    from custom_model_view import GridModelView
    return GridModelView(request, app_label, model_name)
add_route(GridModelFunc, '/grid/:app_label/:model_name/',method='POST')

@valid_user()
def AppMenuFunc(app_label):
    '''
    子系统菜单
    '''
    from sys_view import get_app_nemus
    ret_data = get_app_nemus(app_label)
    if ret_data==None:
        return HTTPError(404, "File does not exist.")
    else:
        return JTemplate('app_menu',nemu_grup = ret_data)
add_route(AppMenuFunc, '/menu/:app_label/',method='POST')

@valid_user()
def MainPageFunc():
    '''
    系统主页面
    '''
    import apps
    from sys_view import get_app_nemus
    ret_data = get_app_nemus(apps.apps_list[0][0])
    return JTemplate('main',apps = apps.apps_list, nemu_grup=ret_data)
add_route(MainPageFunc, '/')