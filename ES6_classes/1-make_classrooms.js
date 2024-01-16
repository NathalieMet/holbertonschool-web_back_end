import ClassRoom from './0-classroom.js';

export default function initializeRooms(Classroom) {
	const classroom_objects = [new ClassRoom(19),
		new ClassRoom(20),
		new ClassRoom(34),]
	return classroom_objects
  }
