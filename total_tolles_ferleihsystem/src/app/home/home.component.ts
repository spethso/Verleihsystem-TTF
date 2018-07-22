import { Component, OnInit } from '@angular/core';
import { NavigationService, Breadcrumb } from '../navigation/navigation-service';
import { JWTService } from '../shared/rest/jwt.service';
import { ApiService } from '../shared/rest/api.service';
import { ApiObject } from '../shared/rest/api-base.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'ttf-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

    lentItems: ApiObject[];

    constructor(private data: NavigationService, private jwt: JWTService, private api: ApiService) { }

    ngOnInit(): void {
        this.data.changeTitle('Total Tolles Ferleihsystem – Home');
        this.data.changeBreadcrumbs([]);
        this.api.getLentItems('errors').subscribe(items => {
            this.lentItems = items;
        });
        Observable.timer(5 * 60 * 1000, 5 * 60 * 1000).subscribe(() => this.api.getLentItems());
    }

    itemOverdue(item: ApiObject): boolean {
        const due = new Date(item.due);
        return due < new Date();
    }

}
