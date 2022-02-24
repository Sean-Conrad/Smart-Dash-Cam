storedStructure = load('D:\Anaconda\Projects\Mobile Net Project\cars_annos.mat');
storedStructure.class_names{1, 174} = 'Ram CV Cargo Van Minivan 2012';
annotations = storedStructure.annotations;
class_names = storedStructure.class_names;
save('D:\Anaconda\Projects\Mobile Net Project\cars_annos.mat', 'annotations', 'class_names');